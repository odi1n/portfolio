from django.db import models

from .custom_user import CustomUser
from .language_type import LanguageType


class Language(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    language_type = models.ForeignKey(LanguageType, verbose_name="Язык", on_delete=models.PROTECT)
    text = models.CharField(verbose_name="Уровень знания", max_length=255)

    class Meta:
        verbose_name = "Знание языков"
        verbose_name_plural = "Знание языков"

    def __str__(self) -> str:
        return self.text
