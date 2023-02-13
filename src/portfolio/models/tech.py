from django.db import models

from .type import CategoryType


class Tech(models.Model):
    category = models.IntegerField(
        verbose_name="Категория", choices=CategoryType.choices
    )
    text = models.CharField("Текст", max_length=255)

    class Meta:
        verbose_name = "Технологии"
        verbose_name_plural = "Технологии"
        # ordering = ['category',
        #             'text']

    def __str__(self):
        return f"{self.get_category_display()}:  {self.text}"
