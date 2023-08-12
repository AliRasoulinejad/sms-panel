from factory import django, fuzzy

from apps.message.enums import MessageStatus


class OutgoingMessageFactory(django.DjangoModelFactory):
    class Meta:
        model = "apps_message.OutgoingMessage"

    message = fuzzy.FuzzyText(length=60)
    receiver_id = fuzzy.FuzzyInteger(low=1, high=3)
    sender_id = fuzzy.FuzzyInteger(low=1, high=3)
    owner_id = fuzzy.FuzzyInteger(low=1, high=3)
    status = fuzzy.FuzzyChoice(choices=MessageStatus.values)
