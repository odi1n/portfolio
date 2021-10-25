from django.db import models
from .portfolio import Portfolio
from .project import Project


class Experience(models.Model):
    portfolio = models.ForeignKey(Portfolio,
                                  verbose_name="Портфолио",
                                  on_delete=models.CASCADE)
    project = models.ForeignKey(Project,
                                verbose_name="Проект",
                                on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание")
    is_enabled = models.BooleanField(verbose_name="Выводить",
                                     default=True)

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = 'Опыт'
        ordering = ['portfolio','project']

    def __str__(self):
        return f'Проект: {self.project}, описание: {self.description[:150]}...'