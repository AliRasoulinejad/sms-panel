from datetime import datetime

from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

from apps.common.fields import JSONSchemaField
from apps.common.models import BaseModel
from apps.user.enums import (
    PersonTypeEnum,
    StatusEnum,
    RequestStatusEnum,
    AuthorizeRequestEnum,
)
from apps.user.schemas.legal_data import legal_data_schema
from apps.utils.validators import cellphone_validator


class UserManager(models.Manager):
    def create_user(self, cellphone, **extra_fields):
        if not cellphone:
            raise "The given username must be set"
        user = self.model(cellphone=cellphone, **extra_fields)
        user.save(using=self._db)

        return user


class User(ExportModelOperationsMixin("user"), BaseModel):
    cellphone = models.CharField(
        "cellphone", max_length=13, unique=True, db_index=True, validators=[cellphone_validator]
    )
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    email = models.EmailField("email", null=True, blank=True)
    person_type = models.PositiveSmallIntegerField(
        "person type", choices=PersonTypeEnum.choices, default=PersonTypeEnum.Real
    )
    status = models.PositiveSmallIntegerField("status", choices=StatusEnum.choices, default=StatusEnum.Deactivate)
    legal_data = JSONSchemaField("authorization", default=dict, schema=legal_data_schema)
    last_login = models.DateTimeField(default=datetime.now)

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.cellphone

    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    @property
    def is_authenticated(self):
        return True


class AuthorizeRequest(ExportModelOperationsMixin("authorize_request"), BaseModel):
    request_type = models.PositiveSmallIntegerField(choices=AuthorizeRequestEnum.choices)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.JSONField("data", default=dict)
    status = models.PositiveSmallIntegerField(choices=RequestStatusEnum.choices, default=RequestStatusEnum.CREATED)

    class Meta:
        db_table = "authorize_requests"
        verbose_name = "احراز هویت"
        verbose_name_plural = "احراز هویت‌ها"

    def __str__(self):
        return f"{self.request_type} for {self.user_id}"
