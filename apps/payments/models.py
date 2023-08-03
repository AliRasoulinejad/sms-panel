from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel
from apps.payments.enums import StatusEnum, GatewayEnum


class Payment(ExportModelOperationsMixin('payment'), BaseModel):
    uid = models.CharField(unique=True, db_index=True)
    status = models.PositiveSmallIntegerField(choices=StatusEnum.choices, default=StatusEnum.Draft)
    amount = models.PositiveIntegerField()
    user = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)
    gateway = models.PositiveSmallIntegerField(choices=GatewayEnum.choices)

    class Meta:
        db_table = "transactions"
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش‌ها"

    def __str__(self):
        return f"{self.amount}"
