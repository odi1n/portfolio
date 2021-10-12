from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name="Название",
                            max_length=255)
    description = models.TextField(verbose_name="Описание проекта",
                                   null=True,
                                   blank=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено',
                                      auto_now=True)
    created_at = models.DateTimeField(verbose_name="Добавлен",
                                      auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = "Проект"
        verbose_name_plural = "Проект"

    def __str__(self):
        return self.name
