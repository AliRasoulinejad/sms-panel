from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.notification.models import Notification
from .services.command import notification_send

@receiver(post_save, sender=Notification)
def update_profile(sender, created, instance, **kwargs) -> Notification:
    if created:
        notification_send(instance)

    return instance
