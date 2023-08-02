from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SupportUser


@admin.register(SupportUser)
class SupportUserAdmin(UserAdmin):
    pass
