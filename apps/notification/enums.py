from django.db.models import IntegerChoices


class NotifType(IntegerChoices):
    SMS = 1
    PushNotification = 2
