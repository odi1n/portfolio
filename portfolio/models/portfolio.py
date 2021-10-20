from django.db import models
from .type import StackType
from .tech import Tech


class Portfolio(models.Model):
    user = models.ForeignKey("users.CustomUser",
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    stack = models.IntegerField(verbose_name="Стэк",
                                choices=StackType.choices)
    tech = models.ManyToManyField(Tech,
                                  verbose_name="Используемые технологии")
    setting = models.JSONField(verbose_name="Настройки",
                               default=dict)

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return f'{self.user} - {self.stack}'