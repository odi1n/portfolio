from django.db import models
from django.utils.translation import ugettext_lazy as _

class CategoryType(models.IntegerChoices):
    OTHER = 0, _('Other')
    LANGUAGE = 1, _('Language')
