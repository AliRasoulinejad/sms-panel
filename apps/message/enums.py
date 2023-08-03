from django.db.models import IntegerChoices

class MessageStatus(IntegerChoices):
    Draft = 0
    Sent = 1
    Cancel = 2
    Reject = 3
