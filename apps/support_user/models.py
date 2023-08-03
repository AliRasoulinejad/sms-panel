from django.contrib.auth.models import AbstractUser
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel


class SupportUser(ExportModelOperationsMixin('support_user'), AbstractUser, BaseModel):
    class Meta(AbstractUser.Meta):
        db_table = "support_users"
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
