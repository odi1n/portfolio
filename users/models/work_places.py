from django.db import models
from django.utils.timezone import now

from .custom_user import CustomUser


class WorkPlace(models.Model):
    user = models.ForeignKey(CustomUser,
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    text = models.CharField(verbose_name="Место работы",
                            help_text="Название компании. Например: Rocket Science",
                            max_length=255)
    whom = models.CharField(verbose_name="Кем работаете",
                            help_text="Например: Разработчик, Архитектор, Программист, ....",
                            max_length=255)
    date_start = models.DateField(verbose_name="Начало работы",
                                  default=now,
                                  editable=True)
    date_end = models.DateField(verbose_name="Конец работы",
                                help_text="Оставить поле пустым, если сейчас работаете",
                                editable=True,
                                null=True,
                                blank=True)

    class Meta:
        verbose_name = "Место работы"
        verbose_name_plural = 'Места работы'

    def __str__(self):
        return self.text
