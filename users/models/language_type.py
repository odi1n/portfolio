from django.db import models


class LanguageType(models.Model):
    text = models.CharField(verbose_name="Язык",
                            max_length=255)

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = 'Языки'

    def __str__(self):
        return self.text
