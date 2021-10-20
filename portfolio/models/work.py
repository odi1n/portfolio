from django.db import models
from .type import ScheduleType


class Work(models.Model):
    grade = models.CharField(verbose_name="Градация",
                             max_length=255)
    salary = models.CharField(verbose_name="Желаемая зарплата",
                              max_length=255)
    post = models.CharField(verbose_name="Желаемая должность",
                            max_length=255)
    travel_time = models.CharField(verbose_name="Время в пути",
                                   max_length=255)
    employment = models.CharField(verbose_name="Занятость",
                                  max_length=255)
    schedule = models.IntegerField(verbose_name="График работы",
                                   choices=ScheduleType.choices)

    class Meta:
        verbose_name = "Место работы"
        verbose_name_plural = 'Место работы'
