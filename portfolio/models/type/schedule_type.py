from django.db import models
from django.utils.translation import ugettext_lazy as _

class ScheduleType(models.IntegerChoices):
    REMOTE = 0, _('Удаленный')
    FULL = 1, _('Полный')
    FLEXIBLE = 2, _('Гибкий')
