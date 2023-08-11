from django.db.models import QuerySet

from apps.phonebook.models import PhoneGroup, Phone


def get_phone(*, instance_id: int, owner_id: int) -> Phone:
    return Phone.objects.filter(id=instance_id, owner_id=owner_id).last()

def list_phone(*, owner_id: int) -> QuerySet[Phone]:
    return Phone.objects.filter(owner_id=owner_id)

def get_phone_group(*, instance_id: int, owner_id: int) -> Phone:
    return PhoneGroup.objects.filter(id=instance_id, owner_id=owner_id).last()

def list_phone_group(*, owner_id: int) -> QuerySet[PhoneGroup]:
    return PhoneGroup.objects.filter(owner_id=owner_id)
