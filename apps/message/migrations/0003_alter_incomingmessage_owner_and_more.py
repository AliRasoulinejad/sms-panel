# Generated by Django 4.2.4 on 2023-08-18 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_user', '0004_authorizerequest'),
        ('apps_sender', '0002_sharesender_alter_sender_unique_together_and_more'),
        ('apps_phonebook', '0001_initial'),
        ('apps_message', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingmessage',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='apps_user.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incomingmessage',
            name='sender',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='apps_sender.sender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outgoingmessage',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='apps_user.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outgoingmessage',
            name='receiver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='apps_phonebook.phone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outgoingmessage',
            name='sender',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='apps_sender.sender'),
            preserve_default=False,
        ),
    ]
