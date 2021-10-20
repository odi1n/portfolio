from django.db import models
from .type import CategoryType


class Tech(models.Model):
    category = models.IntegerField(verbose_name="Пол",
                                   choices=CategoryType.choices)
    text = models.TextField("Текст")

    class Meta:
        verbose_name = "Технологии"
        verbose_name_plural = 'Технологии'
