from django.contrib import admin

from ..models import Experience
from ..models import Work


class ExperienceStackedInline(admin.StackedInline):
    model = Experience
    classes = ["collapse"]
    extra = 1


class WorkStackedInline(admin.StackedInline):
    model = Work
    classes = ["collapse"]
    extra = 1
