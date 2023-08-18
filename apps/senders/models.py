from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel
from .enums import NumberEnum


# TODO: soft delete should handle in future
# TODO: adding "Audit Log"
class Sender(ExportModelOperationsMixin("sender"), BaseModel):
    number = models.CharField(max_length=20, unique=True, db_index=True)
    owner = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=NumberEnum.choices, default=NumberEnum.Requested)

    class Meta:
        db_table = "numbers"
        verbose_name = "سرشماره"
        verbose_name_plural = "سرشماره‌ها"
        unique_together = ("owner", "number")
        indexes = [models.Index("owner", "number", name="idx_senders_owner_id_number")]

    def __str__(self):
        return self.number


class ShareSender(ExportModelOperationsMixin("share_sender"), BaseModel):
    number = models.CharField(max_length=20, unique=True, db_index=True)

    class Meta:
        db_table = "share_numbers"
        verbose_name = "سرشماره مشترک"
        verbose_name_plural = "سرشماره‌های مشترک"

    def __str__(self):
        return self.number
