from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel
from apps.utils.validators import cellphone_validator


class Phone(ExportModelOperationsMixin('phone'), BaseModel):
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=13, validators=[cellphone_validator], editable=False)
    owner = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "phones"
        verbose_name = "شماره موبایل"
        verbose_name_plural = "شماره موبایل ها"
        unique_together = ("phone", "owner")
        indexes = [
            models.Index("phone", "owner_id", name="idx_phones_phone_owner_id")
        ]

    def __str__(self):
        return self.phone

class PhoneGroup(ExportModelOperationsMixin('phone_group'), BaseModel):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Phone, related_query_name="groups")
    owner = models.ForeignKey("apps_user.User", on_delete=models.CASCADE)
    members_count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "groups"
        verbose_name = "گروه"
        verbose_name_plural = "گروه‌ها"

    def __str__(self):
        return self.name

    def recalculate_members_count(self):
        self.members_count = self.members.count()
        self.save()
