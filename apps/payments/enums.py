from django.db import models


class StatusEnum(models.IntegerChoices):
    Draft = 0
    SentToBank = 1
    Accepted = 2
    Rejected = 3

class GatewayEnum(models.IntegerChoices):
    Mellat = 1
