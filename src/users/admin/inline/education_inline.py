from django.contrib import admin

from ...models import Education


class EducationStackedInline(admin.StackedInline):
    model = Education
    classes = ["collapse"]
    extra = 1
