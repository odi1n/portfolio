from django.db import models


class SocialType(models.Model):
    name = models.CharField(
        verbose_name="Название",
        help_text="Например: vk, tg, skype, ds, ...",
        max_length=255,
    )

    class Meta:
        verbose_name = "Соц. сети - виды"
        verbose_name_plural = "Соц. сети - виды"

    def __str__(self) -> str:
        return self.name
