from django.contrib import admin

from .models import Phone, PhoneGroup


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneGroup)
class PhoneGroupAdmin(admin.ModelAdmin):
    pass
