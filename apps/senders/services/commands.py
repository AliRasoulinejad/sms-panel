from apps.senders.enums import RequestTypeEnum
from apps.senders.models import Sender, SenderRequest


def create_sender(*, user_id: int, number: str) -> SenderRequest:
    return SenderRequest.objects.create(number=number, user_id=user_id, request_type=RequestTypeEnum.CREATE)


def delete_sender(
    *,
    instance_id: int,
    owner_id: int,
) -> Sender:
    return Sender.objects.filter(id=instance_id, owner_id=owner_id).delete()


def upgrade_sender(*, instance_id: int, user_id: int) -> SenderRequest:
    return SenderRequest.objects.create(id=instance_id, user_id=user_id, request_type=RequestTypeEnum.UPGRADE)
