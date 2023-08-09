from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.models import BaseModel
from apps.message.enums import MessageStatus


class OutgoingMessage(ExportModelOperationsMixin('outgoing_message'), BaseModel):
    message = models.TextField()
    receiver = models.ForeignKey("apps_phonebook.Phone", on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey("apps_sender.Sender", on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey("apps_user.User", on_delete=models.SET_NULL, null=True)
    status = models.PositiveSmallIntegerField(choices=MessageStatus.choices, default=MessageStatus.Draft)

    class Meta:
        db_table = "outgoing_messages"
        verbose_name = "پیام خروجی"
        verbose_name_plural = "پیام‌های خروجی"


class IncomingMessage(ExportModelOperationsMixin('incoming_message'), BaseModel):
    message = models.TextField()
    sender = models.ForeignKey("apps_sender.Sender", on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey("apps_user.User", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "incoming_messages"
        verbose_name = "پیام ورودی"
        verbose_name_plural = "پیام‌های ورودی"
