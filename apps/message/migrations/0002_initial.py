# Generated by Django 4.2.4 on 2023-08-10 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps_message', '0001_initial'),
        ('apps_user', '0002_user_last_login'),
        ('apps_sender', '0001_initial'),
        ('apps_phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outgoingmessage',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps_phonebook.phone'),
        ),
        migrations.AddField(
            model_name='outgoingmessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps_sender.sender'),
        ),
        migrations.AddField(
            model_name='incomingmessage',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps_user.user'),
        ),
        migrations.AddField(
            model_name='incomingmessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps_sender.sender'),
        ),
    ]
