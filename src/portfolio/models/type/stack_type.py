from django.db import models
from django.utils.translation import ugettext_lazy as _


class StackType(models.IntegerChoices):
    FULLSTACK = 0, _("Fullstack")
    BACKEND = 1, _("Back-End")
    FRONTEND = 2, _("Front-End")
