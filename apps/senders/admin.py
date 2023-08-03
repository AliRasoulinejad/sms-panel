from django.contrib import admin

from .models import Sender


@admin.register(Sender)
class SenderAdmin(admin.ModelAdmin):
    list_display = ("number", "status",)
