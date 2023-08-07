from abc import ABC

from apps.notification.models import Notification, NotifType


class AbstractSMSTemplate(ABC):
    template = ""

    def __prepare_message(self, **kwargs) -> str:
        message = self.template
        for key, value in kwargs.items():
            message = message.replace(f"{[key]}", str(value))

        return message

    def send(self, *, cellphone: str, **kwargs):
        message = self.__prepare_message(**kwargs)
        Notification.objects.create(
            notif_type=NotifType.SMS,
            data={
                "cellphone": cellphone,
                "message": message,
            })
