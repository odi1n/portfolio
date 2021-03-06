from django.db import models
from .type import StackType
from .tech import Tech

def sett_def():
    return {"portfolio": False,
     "work_places": False}

class Portfolio(models.Model):
    user = models.ForeignKey("users.CustomUser",
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    experience_with = models.DateTimeField(verbose_name="Опыт работы с",
                                           help_text="Указать год, с которого начали работать")
    stack = models.IntegerField(verbose_name="Стэк",
                                choices=StackType.choices)
    tech = models.ManyToManyField(Tech,
                                  verbose_name="Используемые технологии")
    setting = models.JSONField(verbose_name="Настройки",
                               default=sett_def())

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return f'{self.user} - {self.stack}'
