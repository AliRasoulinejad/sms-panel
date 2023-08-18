from django.db.models import IntegerChoices


class RequestStatusEnum(IntegerChoices):
    Requested = 0
    SentToProvider = 1
    Rejected = 2
    Accepted = 3
    RejectedByProvider = 4


class RequestTypeEnum(IntegerChoices):
    CREATE = 1
    UPGRADE = 2
