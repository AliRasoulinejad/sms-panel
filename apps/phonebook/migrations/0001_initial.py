# Generated by Django 4.2.4 on 2023-08-03 11:35

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
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(db_index=True, max_length=20, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_user.user')),
            ],
            options={
                'verbose_name': 'شماره موبایل',
                'verbose_name_plural': 'شماره موبایل ها',
                'db_table': 'phones',
            },
            bases=(django_prometheus.models.ExportModelOperationsMixin('phone'), models.Model),
        ),
        migrations.CreateModel(
            name='PhoneGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_user.user')),
                ('phone', models.ManyToManyField(related_name='phones', to='phonebook.phone')),
            ],
            options={
                'verbose_name': 'گروه',
                'verbose_name_plural': 'گروه\u200cها',
                'db_table': 'groups',
            },
            bases=(django_prometheus.models.ExportModelOperationsMixin('phone_group'), models.Model),
        ),
    ]
