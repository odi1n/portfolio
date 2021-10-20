from django.db import models
from .tech import Tech


class Project(models.Model):
    title = models.CharField(verbose_name="Описание",
                             max_length=255)
    link = models.URLField(verbose_name="Ссылка на проект")
    description = models.TextField(verbose_name="Описание")
    tech = models.ManyToManyField(Tech,
                                  verbose_name="Технологии")

    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = 'Проекты'
