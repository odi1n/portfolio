from django.db import models

from .custom_user import CustomUser


class Education(models.Model):
    user = models.ForeignKey(
        CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name="Название учреждения", max_length=255)
    date_start = models.DateField(verbose_name="Начал обучение")
    date_end = models.DateField(verbose_name="Завершил обучение", null=True, blank=True)

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return self.name
