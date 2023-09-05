from django.db import models
from django.utils.translation import ugettext_lazy as _

from .tech import Tech


def sett_def() -> dict[str, bool]:
    return {"portfolio": False, "work_places": False}


class Portfolio(models.Model):
    class StackType(models.IntegerChoices):
        FULLSTACK = 0, _("Fullstack")
        BACKEND = 1, _("Back-End")
        FRONTEND = 2, _("Front-End")

    name = models.CharField(verbose_name="Название", max_length=255, blank=True, null=True)
    user = models.ForeignKey("users.CustomUser", verbose_name="Пользователь", on_delete=models.CASCADE)
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

    def __str__(self) -> str:
        if self.name is not None:
            return f"{self.name}"
        return f"{self.get_stack_display()}"
