from django.test import TestCase

from apps.phonebook.tests.factories import PhoneFactory, PhoneGroupFactory
from apps.user.tests.factories import UserFactory


class PhoneModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user_id = UserFactory().id
        cls.Phone1 = PhoneFactory(name="phone 1", phone="+989101112233", owner_id=user_id)

    def test_phone_str_failure(self):
        self.assertNotEqual(str(self.Phone1), "+989")

    def test_phone_str_success(self):
        self.assertEqual(str(self.Phone1), "+989101112233")

class PhoneGroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user_id = UserFactory().id
        phone1 = PhoneFactory(name="phone 1", owner_id=user_id)
        phone2 = PhoneFactory(name="phone 2", owner_id=user_id)
        cls.PhoneGroup = PhoneGroupFactory(name="phone group 1", owner_id=user_id)
        cls.PhoneGroup.members.add(phone1, phone2)


    def test_phone_group_str_failure(self):
        self.assertNotEqual(str(self.PhoneGroup), "phone group")

    def test_phone_group_str_success(self):
        self.assertEqual(str(self.PhoneGroup), "phone group 1")

    def test_phone_group_recalculate_members_count_success(self):
        self.assertEqual(self.PhoneGroup.members_count, 0)
        self.PhoneGroup.recalculate_members_count()
        self.assertEqual(self.PhoneGroup.members_count, 2)

    def test_phone_group_recalculate_members_count_success2(self):
        self.assertEqual(self.PhoneGroup.members_count, 0)
        self.PhoneGroup.recalculate_members_count()
        self.assertEqual(self.PhoneGroup.members_count, 2)
