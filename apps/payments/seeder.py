import string

from factory import django, fuzzy

from apps.payments.enums import StatusEnum, GatewayEnum


class PaymentFactory(django.DjangoModelFactory):
    class Meta:
        model = 'apps_payments.Payment'

    uid = fuzzy.FuzzyText(length=20, chars=string.ascii_letters + string.digits)
    status = fuzzy.FuzzyChoice(choices=StatusEnum.values)
    amount = fuzzy.FuzzyInteger(low=100, high=100000)
    user_id = fuzzy.FuzzyInteger(low=1, high=3)
    gateway = fuzzy.FuzzyChoice(choices=GatewayEnum.values)
