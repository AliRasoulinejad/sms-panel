from apps.notification.enums import NotifType
from apps.notification.models import Notification
from config.settings.sms_modules import sms_module


def notification_send(notification: Notification):
    if notification.notif_type == NotifType.SMS:

        sms_module.send_message(
            cellphone=notification.data["cellphone"],
            message=notification.data["message"],
        )
    # TODO: make decision to remove this or add the support of push notification
    # elif notification.notif_type == NotifType.PushNotification:
    #     push_notif_module.notify(
    #         token=notification.data["token"],
    #         message=notification.data["message"],
    #     )
    else:
        raise ValueError("wrong notification type")
