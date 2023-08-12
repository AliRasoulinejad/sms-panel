from django.apps import AppConfig


class NotificationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.notification"
    label = "apps_notification"
    verbose_name = "اعلان‌ها"

    def ready(self) -> None:
        from . import signals  # noqa

        super().ready()
