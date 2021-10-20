from django.db import models
from .type import StackType
from .tech import Tech
from .work import Work


class Portfolio(models.Model):
    user = models.ForeignKey("users.CustomUser",
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    stack = models.IntegerField(verbose_name="Стэк",
                                choices=StackType.choices)

    work = models.ManyToManyField(Work,
                                  verbose_name="Места работы")
    tech = models.ManyToManyField(Tech,
                                  verbose_name="Технологии")
    setting = models.JSONField(verbose_name="Настройки",
                               default=dict)

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = 'Портфолио'
