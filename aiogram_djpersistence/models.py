from aiogram.fsm.storage.base import StorageKey, DefaultKeyBuilder
from django.db import models


class PersistentStorageManager(models.Manager):
    def get_item(self, key: StorageKey):
        return self.filter(
            bot_id=key.bot_id,
            chat_id=key.chat_id,
            user_id=key.user_id,
            thread_id=key.thread_id or 0,
            business_connection_id=key.business_connection_id or "",
            destiny=key.destiny,
        ).first()

    async def aget_item(self, key: StorageKey):
        return await self.filter(
            bot_id=key.bot_id,
            chat_id=key.chat_id,
            user_id=key.user_id,
            thread_id=key.thread_id or 0,
            business_connection_id=key.business_connection_id or "",
            destiny=key.destiny,
        ).afirst()


class PersistentStorage(models.Model):
    bot_id = models.BigIntegerField()
    chat_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    thread_id = models.BigIntegerField(default=0)
    business_connection_id = models.CharField(max_length=255, blank=True)
    destiny = models.TextField(max_length=255)

    state = models.TextField(null=True, blank=True)  # noqa: DJ001
    data = models.JSONField(null=True, blank=True)

    objects = PersistentStorageManager()

    class Meta:
        indexes = [
            models.Index(fields=["bot_id", "chat_id", "user_id", "thread_id", "business_connection_id", "destiny"]),
        ]
        unique_together = ["bot_id", "chat_id", "user_id", "thread_id", "business_connection_id", "destiny"]

    def __str__(self):
        key = StorageKey(
            bot_id=self.bot_id,
            chat_id=self.chat_id,
            user_id=self.user_id,
            thread_id=self.thread_id,
            business_connection_id=self.business_connection_id,
            destiny=self.destiny,
        )
        return DefaultKeyBuilder(with_bot_id=True, with_business_connection_id=True, with_destiny=True).build(key)
