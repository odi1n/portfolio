from django.db import models
from .type import ScheduleType
from .portfolio import Portfolio


class Work(models.Model):
    portfolio = models.ForeignKey(Portfolio,
                                  verbose_name="Порфолио",
                                  on_delete=models.CASCADE)
    grade = models.CharField(verbose_name="Градация",
                             help_text="Например: Junior, Middle, Senio, DevOps, Архитектор, ...",
                             max_length=255)
    salary = models.IntegerField(verbose_name="Желаемая зарплата",
                                 default=0,
                                 null=True,
                                 blank=True)
    post = models.CharField(verbose_name="Желаемая должность",
                            max_length=255,
                            null=True,
                            blank=True)
    travel_time = models.CharField(verbose_name="Время в пути",
                                   max_length=255,
                                   null=True,
                                   blank=True)
    employment = models.CharField(verbose_name="Занятость",
                                  max_length=255,
                                  null=True,
                                  blank=True)
    schedule = models.IntegerField(verbose_name="График работы",
                                   choices=ScheduleType.choices,
                                   null=True,
                                   blank=True)

    class Meta:
        verbose_name = "Пожелания для устройства"
        verbose_name_plural = 'Пожелания для устройства'
