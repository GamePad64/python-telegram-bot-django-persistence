from django.db import models


class BaseData(models.Model):
    namespace = models.CharField(max_length=255, blank=True, null=False)

    class Meta:
        abstract = True


class BotData(BaseData):
    data = models.JSONField()

    def __str__(self):
        return self.namespace or "<BotData>"


class ChatData(BaseData):
    chat_id = models.BigIntegerField(null=False, blank=False)
    data = models.JSONField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["namespace", "chat_id"], name="unique_chat_id")]
        indexes = [models.Index(fields=["namespace", "chat_id"])]

    def __str__(self):
        if self.namespace:
            return f"{self.namespace}:{self.chat_id}"
        else:
            return str(self.chat_id)


class UserData(BaseData):
    user_id = models.BigIntegerField(null=False, blank=False)
    data = models.JSONField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["namespace", "user_id"], name="unique_user_id")]
        indexes = [models.Index(fields=["namespace", "user_id"])]

    def __str__(self):
        if self.namespace:
            return f"{self.namespace}:{self.user_id}"
        else:
            return str(self.user_id)


class CallbackData(BaseData):
    data = models.JSONField()

    def __str__(self):
        return self.namespace or "<CallbackData>"


class ConversationData(BaseData):
    name = models.CharField(max_length=255, blank=True, null=False)
    key = models.TextField()  # stringified JSON here!
    state = models.JSONField(null=True, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["namespace", "name", "key"], name="unique_conversation_data")]
        indexes = [models.Index(fields=["namespace", "name", "key"])]

    def __str__(self):
        if self.namespace:
            return f"{self.namespace}:{self.name}:{self.key}"
        else:
            return f"{self.name}:{self.key}"
