# Generated by Django 4.2.4 on 2023-08-03 16:29

from django.db import migrations, models
import django.db.models.deletion
import django_prometheus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uid', models.CharField(db_index=True, unique=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Senttobank'), (2, 'Accepted'), (3, 'Rejected')], default=0)),
                ('amount', models.PositiveIntegerField()),
                ('gateway', models.PositiveSmallIntegerField(choices=[(1, 'Mellat')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_user.user')),
            ],
            options={
                'verbose_name': 'تراکنش',
                'verbose_name_plural': 'تراکنش\u200cها',
                'db_table': 'transactions',
            },
            bases=(django_prometheus.models.ExportModelOperationsMixin('payment'), models.Model),
        ),
    ]
