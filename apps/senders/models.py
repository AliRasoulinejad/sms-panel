from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel
from .enums import NumberEnum


class Sender(ExportModelOperationsMixin('sender'), BaseModel):
    number = models.CharField(max_length=20, unique=True, db_index=True)
    owner = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=NumberEnum.choices, default=NumberEnum.Requested)

    class Meta:
        db_table = "numbers"
        verbose_name = "سرشماره"
        verbose_name_plural = "سرشماره‌ها"

    def __str__(self):
        return self.number
