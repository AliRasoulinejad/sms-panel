import string

from factory import django, fuzzy


class SupportUserFactory(django.DjangoModelFactory):
    class Meta:
        model = "apps_support_user.SupportUser"

    username = fuzzy.FuzzyText(length=10)
    first_name = fuzzy.FuzzyText(length=10)
    last_name = fuzzy.FuzzyText(length=10)
    email = fuzzy.FuzzyText(length=10, suffix="@e.mail", chars=string.ascii_lowercase + string.digits)
    is_staff = True
    is_active = True
