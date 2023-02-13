from django.db import models
from .type import StackType
from .tech import Tech


def sett_def():
    return {"portfolio": False, "work_places": False}


class Portfolio(models.Model):
    name = models.CharField(
        verbose_name="Название", max_length=255, blank=True, null=True
    )
    user = models.ForeignKey(
        "users.CustomUser", verbose_name="Пользователь", on_delete=models.CASCADE
    )
    experience_with = models.DateField(
        verbose_name="Опыт работы с",
        help_text="Указать год, с которого начали работать",
    )
    stack = models.IntegerField(verbose_name="Стэк", choices=StackType.choices)
    tech = models.ManyToManyField(Tech, verbose_name="Используемые технологии")
    setting = models.JSONField(verbose_name="Настройки", default=sett_def())

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"

    def __str__(self):
        if self.name is not None:
            return f"{self.name}"
        return f"{self.get_stack_display()}"
