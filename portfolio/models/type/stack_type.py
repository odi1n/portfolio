from django.db import models
from django.utils.translation import ugettext_lazy as _

class StackType(models.IntegerChoices):
    FULLSTACK = 0, _('Fullsack')
    BACKEND = 1, _('Backend')
    FRONTEND = 2, _('Frontend')
