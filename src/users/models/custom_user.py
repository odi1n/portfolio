from django.contrib.auth.models import AbstractUser
from django.db import models

from .type import SexType


# Create your models here.
class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""

    first_name = models.CharField(verbose_name="Имя", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    middle_name = models.CharField(verbose_name="Отчество", max_length=150, blank=True)
    last_career_meeting = models.DateField(
        verbose_name="Последняя карьерная встреча", null=True, blank=True
    )
    sex = models.IntegerField(
        verbose_name="Пол", choices=SexType.choices, default=SexType.MALE
    )
    age = models.IntegerField(verbose_name="Возраст", default=0)

    @property
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    @property
    def get_name(self):
        return f"{self.last_name} {self.first_name}"
