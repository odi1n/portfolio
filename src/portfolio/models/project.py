from django.db import models
from .tech import Tech


class Project(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    link = models.URLField(verbose_name="Ссылка на проект", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    tech = models.ManyToManyField(Tech, verbose_name="Технологии проекта")

    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"
        ordering = ["-id"]

    def __str__(self):
        return self.title
