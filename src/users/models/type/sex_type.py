from django.db import models
from django.utils.translation import ugettext_lazy as _


class SexType(models.IntegerChoices):
    MALE = 0, _("Мужчина")
    FEMALE = 1, _("Женщина")
