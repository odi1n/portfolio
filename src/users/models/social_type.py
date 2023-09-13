from django.db import models


class SocialType(models.Model):
    name = models.CharField(
        verbose_name="Название",
        help_text="Например: vk, tg, skype, ds, ...",
        max_length=255,
    )

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"

    def __str__(self) -> str:
        return self.name
