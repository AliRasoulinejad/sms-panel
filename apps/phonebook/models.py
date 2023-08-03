from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel


class Phone(ExportModelOperationsMixin('phone'), BaseModel):
    phone = models.CharField(max_length=20, unique=True, db_index=True)
    owner = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "phones"
        verbose_name = "شماره موبایل"
        verbose_name_plural = "شماره موبایل ها"

    def __str__(self):
        return self.phone

class PhoneGroup(ExportModelOperationsMixin('phone_group'), BaseModel):
    name = models.CharField(max_length=50)
    phone = models.ManyToManyField(Phone, related_name="phones")
    owner = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "groups"
        verbose_name = "گروه"
        verbose_name_plural = "گروه‌ها"

    def __str__(self):
        return self.name
