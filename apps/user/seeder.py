import string

from factory import django, fuzzy

from apps.user.enums import PersonTypeEnum, StatusEnum


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = 'apps_user.User'
        django_get_or_create = ("cellphone", "first_name", "last_name")

    cellphone = fuzzy.FuzzyText(prefix="+989", length=9, chars=string.digits)
    first_name = fuzzy.FuzzyText(length=10)
    last_name = fuzzy.FuzzyText(length=10)
    email = fuzzy.FuzzyText(length=10, suffix="@e.mail", chars=string.ascii_lowercase + string.digits)
    person_type = fuzzy.FuzzyChoice(choices=PersonTypeEnum.values)
    status = fuzzy.FuzzyChoice(choices=StatusEnum.values)
