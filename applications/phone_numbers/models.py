from django.db import models

from applications.common.models import BaseModel
from .enums import NumberEnum


class Numbers(BaseModel):
    number = models.CharField(max_length=20, unique=True, db_index=True)
    owner = models.ForeignKey("applications_user.User", on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=NumberEnum.choices, default=NumberEnum.Requested)

    class Meta:
        db_table = "numbers"
        verbose_name = "سرشماره"
        verbose_name_plural = "سرشماره‌ها"

    def __str__(self):
        return self.number
