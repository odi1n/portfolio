from django.contrib import admin

from ...models import Experience


class ExperienceStackedInline(admin.StackedInline):
    model = Experience
    classes = ["collapse"]
    extra = 1
