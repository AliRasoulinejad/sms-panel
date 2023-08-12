import string

from factory import django, fuzzy

from apps.senders.enums import NumberEnum


class SenderFactory(django.DjangoModelFactory):
    class Meta:
        model = "apps_sender.Sender"

    number = fuzzy.FuzzyText(length=12, chars=string.digits)
    owner_id = fuzzy.FuzzyInteger(low=1, high=3)
    status = fuzzy.FuzzyChoice(choices=NumberEnum.values)
