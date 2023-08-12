import string

from factory import django, fuzzy


class PhoneFactory(django.DjangoModelFactory):
    class Meta:
        model = "apps_phonebook.Phone"

    name = fuzzy.FuzzyText(length=20, chars=string.ascii_letters)
    phone = fuzzy.FuzzyText(prefix="+989", length=9, chars=string.digits)
    owner_id = fuzzy.FuzzyInteger(low=1, high=3)


class PhoneGroupFactory(django.DjangoModelFactory):
    class Meta:
        model = "apps_phonebook.PhoneGroup"

    name = fuzzy.FuzzyText(length=20, chars=string.ascii_letters)
    owner_id = fuzzy.FuzzyInteger(low=1, high=3)
