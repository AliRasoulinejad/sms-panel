from factory import django, fuzzy

from apps.notification.enums import NotifType


class NotificationFactory(django.DjangoModelFactory):
    class Meta:
        model = "apps_notification.Notification"

    notif_type = fuzzy.FuzzyChoice(choices=NotifType.values)
    user_id = fuzzy.FuzzyInteger(low=1, high=3)
    # TODO: fix json fake data
    # data = json.dumps({
    #     "cellphone": fuzzy.FuzzyText(prefix="+989", length=9, chars=string.digits),
    #     "message": fuzzy.FuzzyText(length=60, chars=string.ascii_letters + string.digits),
    # }, cls=DjangoJSONEncoder)
