from typing import Any

from aiogram.fsm.storage.base import BaseStorage, StorageKey, StateType, State
from asgiref.sync import sync_to_async

from .models import PersistentStorage
from django.db import transaction


class DjangoStorage(BaseStorage):
    def __init__(self) -> None:
        pass

    async def close(self) -> None:
        pass

    async def set_state(
        self,
        key: StorageKey,
        state: StateType = None,
    ) -> None:
        @transaction.atomic
        def _helper():
            if state is not None:
                PersistentStorage.objects.update_or_create(
                    bot_id=key.bot_id,
                    chat_id=key.chat_id,
                    user_id=key.user_id,
                    thread_id=key.thread_id or 0,
                    business_connection_id=key.business_connection_id or "",
                    destiny=key.destiny,
                    defaults={"state": state.state if isinstance(state, State) else state},
                )
            else:
                item = PersistentStorage.objects.get_item(key)
                if item and not item.data:
                    item.delete()

        await sync_to_async(_helper)()

    async def get_state(self, key: StorageKey) -> str | None:
        item = await PersistentStorage.objects.aget_item(key)
        return item.state if item else None

    async def set_data(self, key: StorageKey, data: dict[str, Any]) -> None:
        @transaction.atomic
        def _helper():
            if data is not None:
                PersistentStorage.objects.update_or_create(
                    bot_id=key.bot_id,
                    chat_id=key.chat_id,
                    user_id=key.user_id,
                    thread_id=key.thread_id or 0,
                    business_connection_id=key.business_connection_id or "",
                    destiny=key.destiny,
                    defaults={"data": data},
                )
            else:
                item = PersistentStorage.objects.get_item(key)
                if item and not item.state:
                    item.delete()

        await sync_to_async(_helper)()

    async def get_data(self, key: StorageKey) -> dict[str, Any]:
        item = await PersistentStorage.objects.aget_item(key)
        return item.data if item and item.data else {}
