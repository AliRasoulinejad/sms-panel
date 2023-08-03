from django.contrib import admin

from apps.message.models import IncomingMessage, OutgoingMessage


@admin.register(OutgoingMessage)
class OutgoingMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(IncomingMessage)
class IncomingMessageAdmin(admin.ModelAdmin):
    pass
