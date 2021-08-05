from django.contrib import admin

from .models import BotData, CallbackData, ChatData, ConversationData, UserData


@admin.register(BotData)
class BotDataAdmin(admin.ModelAdmin):
    list_display = ("namespace", "data")


@admin.register(ChatData)
class ChatDataAdmin(admin.ModelAdmin):
    list_display = ("namespace", "chat_id")


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ("namespace", "user_id")


@admin.register(CallbackData)
class CallbackDataAdmin(admin.ModelAdmin):
    list_display = ("namespace", "data")


@admin.register(ConversationData)
class ConversationDataAdmin(admin.ModelAdmin):
    list_display = ("namespace", "name", "key")
