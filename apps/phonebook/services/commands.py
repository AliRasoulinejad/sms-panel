from typing import OrderedDict

from apps.phonebook.models import PhoneGroup, Phone


def create_phone(*, owner_id: int, name: str, phone: str) -> Phone:
    return Phone.objects.create(name=name, phone=phone, owner_id=owner_id)

def update_phone(*, instance_id: int, owner_id: int, name: str) -> Phone:
    return Phone.objects.filter(id=instance_id, owner_id=owner_id).update(name=name)

def delete_phone(*, instance_id: int, owner_id: int) -> Phone:
    return Phone.objects.filter(id=instance_id, owner_id=owner_id).delete()

def create_phone_group(*, owner_id: int, name: str) -> PhoneGroup:
    return PhoneGroup.objects.create(name=name, owner_id=owner_id)

def update_phone_group(*, instance_id: int, owner_id: int, name: str) -> PhoneGroup:
    return PhoneGroup.objects.filter(id=instance_id, owner_id=owner_id).update(name=name)

def delete_phone_group(*, instance_id: int, owner_id: int) -> None:
    return PhoneGroup.objects.filter(id=instance_id, owner_id=owner_id).delete()

def add_members_to_phone_group(*, instance_id: int, owner_id: int, members: list[OrderedDict]) -> None:
    exists_phones = Phone.objects.filter(phone__in=[member["phone"] for member in members], owner_id=owner_id).values_list("phone", flat=True)
    added_phones = [
        Phone(name=member["name"], phone=member["phone"], owner_id=owner_id)
        for member in members
        if member["phone"] not in exists_phones
    ]
    Phone.objects.bulk_create(added_phones)
    phones = Phone.objects.filter(phone__in=[member["phone"] for member in members], owner_id=owner_id)
    PhoneGroup.objects.filter(id=instance_id, owner_id=owner_id).last().members.add(*phones)
