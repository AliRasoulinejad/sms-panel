from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel
from apps.notification.enums import NotifType


class Notification(ExportModelOperationsMixin("notification"), BaseModel):
    notif_type = models.PositiveSmallIntegerField(choices=NotifType.choices)
    user = models.ForeignKey("apps_user.User", on_delete=models.SET_NULL, null=True)
    data = models.JSONField(default=dict)
    result = models.JSONField(default=dict)

    class Meta:
        db_table = "notification"
        verbose_name = "اعلان"
        verbose_name_plural = "اعلان‌ها"

    def __str__(self) -> str:
        return f"{self.notif_type} to {self.user_id}"
