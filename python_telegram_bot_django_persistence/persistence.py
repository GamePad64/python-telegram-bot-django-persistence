import json
from collections import defaultdict
from typing import DefaultDict, Optional, Tuple, cast

from telegram.ext import BasePersistence
from telegram.ext.utils.types import BD, CD, UD, CDCData, ConversationDict

from .models import BotData, CallbackData, ChatData, ConversationData, UserData


class DjangoPersistence(BasePersistence[UD, CD, BD]):
    def __init__(
        self,
        namespace: str = "",
        store_user_data: bool = True,
        store_chat_data: bool = True,
        store_bot_data: bool = True,
        store_callback_data: bool = False,
    ):
        super().__init__(
            store_user_data=store_user_data,
            store_chat_data=store_chat_data,
            store_bot_data=store_bot_data,
            store_callback_data=store_callback_data,
        )
        self._namespace = namespace

    def get_bot_data(self) -> BD:
        try:
            return BotData.objects.get(namespace=self._namespace).data
        except BotData.DoesNotExist:
            return {}

    def update_bot_data(self, data: BD) -> None:
        BotData.objects.update_or_create(namespace=self._namespace, defaults={"data": data})

    def refresh_bot_data(self, bot_data: BD) -> None:
        if isinstance(bot_data, dict):
            orig_keys = set(bot_data.keys())
            bot_data.update(self.get_bot_data())
            for key in orig_keys - set(bot_data.keys()):
                bot_data.pop(key)

    def get_chat_data(self) -> DefaultDict[int, CD]:
        return defaultdict(
            dict, {data.chat_id: data.data for data in ChatData.objects.filter(namespace=self._namespace)}
        )

    def update_chat_data(self, chat_id: int, data: CD) -> None:
        ChatData.objects.update_or_create(namespace=self._namespace, chat_id=chat_id, defaults={"data": data})

    def refresh_chat_data(self, chat_id: int, chat_data: CD) -> None:
        try:
            if isinstance(chat_data, dict):
                orig_keys = set(chat_data.keys())
                chat_data.update(ChatData.objects.get(namespace=self._namespace, chat_id=chat_id).data)
                for key in orig_keys - set(chat_data.keys()):
                    chat_data.pop(key)
        except ChatData.DoesNotExist:
            pass

    def get_user_data(self) -> DefaultDict[int, UD]:
        return defaultdict(
            dict, {data.user_id: data.data for data in UserData.objects.filter(namespace=self._namespace)}
        )

    def update_user_data(self, user_id: int, data: UD) -> None:
        UserData.objects.update_or_create(namespace=self._namespace, user_id=user_id, defaults={"data": data})

    def refresh_user_data(self, user_id: int, user_data: UD) -> None:
        try:
            if isinstance(user_data, dict):
                orig_keys = set(user_data.keys())
                user_data.update(UserData.objects.get(namespace=self._namespace, user_id=user_id).data)
                for key in orig_keys - set(user_data.keys()):
                    user_data.pop(key)
        except UserData.DoesNotExist:
            pass

    def get_callback_data(self) -> Optional[CDCData]:
        try:
            cdcdata_json = CallbackData.objects.get(namespace=self._namespace)
            # Before asking me wtf is this, just check DictPersistence
            return cast(CDCData, ([(one, float(two), three) for one, two, three in cdcdata_json[0]], cdcdata_json[1]))
        except CallbackData.DoesNotExist:
            return None

    def update_callback_data(self, data: CDCData) -> None:
        CallbackData.objects.update_or_create(namespace=self._namespace, defaults=data)

    def get_conversations(self, name: str) -> ConversationDict:
        return {
            tuple(json.loads(data.key)): data.state
            for data in ConversationData.objects.filter(namespace=self._namespace, name=name)
        }

    def update_conversation(self, name: str, key: Tuple[int, ...], new_state: Optional[object]) -> None:
        ConversationData.objects.update_or_create(
            namespace=self._namespace,
            name=name,
            key=json.dumps(key, sort_keys=True),
            defaults={"state": new_state},
        )

    def flush(self) -> None:
        pass
