from django.db.models import IntegerChoices


class PersonTypeEnum(IntegerChoices):
    Real = 1
    Legal = 2


class StatusEnum(IntegerChoices):
    Deactivate = 0
    Activate = 1
