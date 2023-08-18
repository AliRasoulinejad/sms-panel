from django.db.models import QuerySet

from apps.senders.models import Sender


def get_sender(*, instance_id: int, owner_id: int) -> Sender:
    return Sender.objects.filter(id=instance_id, owner_id=owner_id).last()


def list_senders(*, owner_id: int) -> QuerySet[Sender]:
    return Sender.objects.filter(owner_id=owner_id)
