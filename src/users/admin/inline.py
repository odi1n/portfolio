from django.contrib import admin

from ..models import Education, Language, Social, WorkPlace


class EducationStackedInline(admin.StackedInline):
    model = Education
    classes = ["collapse"]
    extra = 1


class LanguageStackedInline(admin.StackedInline):
    model = Language
    classes = ["collapse"]
    extra = 0


class SocialStackedInline(admin.StackedInline):
    model = Social
    classes = ["collapse"]
    extra = 0


class WorkPlaceStackedInline(admin.StackedInline):
    model = WorkPlace
    classes = ["collapse"]
    extra = 0
