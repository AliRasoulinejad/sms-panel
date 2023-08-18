from django.db.models import IntegerChoices


class PersonTypeEnum(IntegerChoices):
    Real = 1
    Legal = 2


class StatusEnum(IntegerChoices):
    Deactivate = 0
    Activate = 1


class AuthorizeRequestEnum(IntegerChoices):
    LEGAL = 1
    FINANCIAL = 2


class RequestStatusEnum(IntegerChoices):
    CREATED = 0
    ACCEPTED = 1
    REJECTED = 2
