from abc import ABC

from apps.notification.models import Notification, NotifType


class AbstractSMSTemplate(ABC):
    template = ""

    @classmethod
    def __prepare_message(cls, **kwargs) -> str:
        message = cls.template
        for key, value in kwargs.items():
            message = message.replace(f"{[key]}", str(value))

        return message

    @classmethod
    def send(cls, *, user_id: int, cellphone: str, **kwargs):
        message = cls.__prepare_message(**kwargs)
        Notification.objects.create(
            notif_type=NotifType.SMS,
            user_id=user_id,
            data={
                "cellphone": cellphone,
                "message": message,
            },
        )
