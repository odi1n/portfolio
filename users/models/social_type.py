from django.db import models
from .custom_user import CustomUser


class SocialType(models.Model):
    name = models.CharField(verbose_name="Название",
                            max_length=255)

    class Meta:
        verbose_name = "Социальный тип"
        verbose_name_plural = 'Социальные типы'