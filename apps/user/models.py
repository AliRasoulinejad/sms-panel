from django.contrib.auth.hashers import make_password
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from result import Ok, Err

from apps.common.models import BaseModel


class UserManager(models.Manager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            return Err("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return Ok(user)


class User(ExportModelOperationsMixin('user'), BaseModel):
    cellphone = models.CharField("cellphone", max_length=13, unique=True, db_index=True)
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)

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
