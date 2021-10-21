from django.db import models


class SocialType(models.Model):
    name = models.CharField(verbose_name="Название",
                            help_text="Например: vk, tg, skype, ds, ...",
                            max_length=255)

    class Meta:
        verbose_name = "Социальный тип"
        verbose_name_plural = 'Социальные типы'

    def __str__(self):
        return self.name