from django.contrib import admin

from .models import Numbers


@admin.register(Numbers)
class NumberAdmin(admin.ModelAdmin):
    fields = ("number", "status",)
