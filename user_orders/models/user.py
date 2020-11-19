from django.contrib.auth.models import AbstractUser
from django.db import models

from . import Order


class User(AbstractUser):
    birth_date = models.DateField(null=True, verbose_name='birth date')
    registration_date = models.DateField(null=True, verbose_name='registration date')
    order = models.ForeignKey(Order, models.SET_NULL, null=True, blank=True, )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

