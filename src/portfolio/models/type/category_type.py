from django.db import models
from django.utils.translation import ugettext_lazy as _


class CategoryType(models.IntegerChoices):
    PROGRAMS_LANGUAGE = 0, _("Язык программирования/Разметка")
    FRAMEWORK = 1, _("Фреймворк")
    LIBRARIES = 2, _("Библиотека")
    DBMS = 3, _("DBMS")
    CLOUD_SERVICE = 4, _("Cloud - сервис")
    OTHER = 5, _("Другое")
    DEVELOPMENT_TOOL = 6, _("Инструменты разработки")
    APP_TYPE = 7, _("App type")
