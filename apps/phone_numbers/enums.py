from django.db import models


class NumberEnum(models.IntegerChoices):
    Requested = 0
    SentToProvider = 1
    Rejected = 2
    Accepted = 3
    RejectedByProvider = 4
