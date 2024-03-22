from django.contrib import admin
from .models import Message, ChatRoom


class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", 'timestamp')
    list_filter = ("sender", "timestamp")


class ChatRoomAdmin(admin.ModelAdmin):
    list_filter = ("participants",)


admin.site.register(Message, MessageAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)
