import string

from factory import django, fuzzy


class PhoneFactory(django.DjangoModelFactory):
    class Meta:
        model = 'apps_phonebook.Phone'

    phone = fuzzy.FuzzyText(length=12, chars=string.digits)
    owner_id = fuzzy.FuzzyInteger(low=1, high=3)
