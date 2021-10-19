from django.db import models


class Project(models.Model):
    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = 'Проекты'
