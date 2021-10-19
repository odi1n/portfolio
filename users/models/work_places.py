from django.db import models
from .custom_user import CustomUser


class WorkPlace(models.Model):
    user = models.ForeignKey(CustomUser,
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Место работы")

    class Meta:
        verbose_name = "Место работы"
        verbose_name_plural = 'Места работы'
