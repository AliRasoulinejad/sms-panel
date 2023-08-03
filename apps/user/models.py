from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator

from django.db import models
from django.utils.regex_helper import _lazy_re_compile
from django_prometheus.models import ExportModelOperationsMixin
from result import Ok, Err

from apps.common.models import BaseModel
from apps.user.enums import PersonTypeEnum, StatusEnum

cellphone_validator = RegexValidator(
    _lazy_re_compile(r"^\+989\d{9}$"),
    message="Enter a valid cellphone",
    code="invalid",
)


class UserManager(models.Manager):
    def create_user(self, cellphone, **extra_fields):
        if not cellphone:
            raise "The given username must be set"
        user = self.model(cellphone=cellphone, **extra_fields)
        user.save(using=self._db)

        return user


class User(ExportModelOperationsMixin('user'), BaseModel):
    cellphone = models.CharField("cellphone", max_length=13, unique=True, db_index=True, validators=[cellphone_validator])
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    email = models.EmailField("email", null=True, blank=True)
    person_type = models.PositiveSmallIntegerField(
        "person type", choices=PersonTypeEnum.choices, default=PersonTypeEnum.Real
    )
    status = models.PositiveSmallIntegerField("status", choices=StatusEnum.choices, default=StatusEnum.Deactivate)
    legal_data = models.JSONField("authorization", default=dict)

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
