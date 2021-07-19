from django.contrib import admin

from .models import (
    BotData,
    CallbackData,
    ChatData,
    ConversationData,
    UserData,
)

admin.site.register(BotData)
admin.site.register(ChatData)
admin.site.register(UserData)
admin.site.register(CallbackData)
admin.site.register(ConversationData)
