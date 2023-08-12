from django.core.management.base import BaseCommand

from apps.message.models import OutgoingMessage
from apps.message.seeder import OutgoingMessageFactory
from apps.notification.models import Notification
from apps.notification.seeder import NotificationFactory
from apps.payments.models import Payment
from apps.payments.seeder import PaymentFactory
from apps.phonebook.models import Phone, PhoneGroup
from apps.phonebook.tests.factories import PhoneFactory, PhoneGroupFactory
from apps.senders.models import Sender
from apps.senders.seeder import SenderFactory
from apps.support_user.models import SupportUser
from apps.support_user.seeder import SupportUserFactory
from apps.user.models import User
from apps.user.tests.factories import UserFactory


class Command(BaseCommand):
    help = "Seed the database with random data"
    default_number = 3

    def handle(self, *args, **options):
        User.objects.bulk_create(UserFactory.build_batch(self.default_number))
        self.stdout.write(self.style.SUCCESS("Database seeded with user successfully"))

        SupportUser.objects.bulk_create(SupportUserFactory.build_batch(self.default_number))
        self.stdout.write(self.style.SUCCESS("Database seeded with support_user successfully"))

        Sender.objects.bulk_create(SenderFactory.build_batch(self.default_number))
        self.stdout.write(self.style.SUCCESS("Database seeded with sender successfully"))

        Phone.objects.bulk_create(PhoneFactory.build_batch(self.default_number))
        self.stdout.write(self.style.SUCCESS("Database seeded with phone successfully"))

        pg = PhoneGroup.objects.bulk_create(PhoneGroupFactory.build_batch(1))
        pg[0].members.add(*Phone.objects.all())
        self.stdout.write(self.style.SUCCESS("Database seeded with phone successfully"))

        Payment.objects.bulk_create(PaymentFactory.build_batch(self.default_number))
        self.stdout.write(self.style.SUCCESS("Database seeded with payment successfully"))

        Notification.objects.bulk_create(NotificationFactory.build_batch(self.default_number))
        self.stdout.write(self.style.SUCCESS("Database seeded with notification successfully"))

        OutgoingMessage.objects.bulk_create(OutgoingMessageFactory.build_batch(self.default_number))
        self.stdout.write(self.style.SUCCESS("Database seeded with outgoing_message successfully"))
