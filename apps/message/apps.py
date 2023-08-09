from django.apps import AppConfig


class MessageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.message'
    label = 'apps_message'
    verbose_name = "پیام‌ها"
