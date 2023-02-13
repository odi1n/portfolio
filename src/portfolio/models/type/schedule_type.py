from django.db import models
from django.utils.translation import ugettext_lazy as _


class ScheduleType(models.IntegerChoices):
    REMOTE = 0, _("удаленный")
    FULL = 1, _("полный")
    FLEXIBLE = 2, _("гибкий")
