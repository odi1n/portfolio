from django.contrib import admin

from ...models import WorkPlace


class WorkPlaceStackedInline(admin.StackedInline):
    model = WorkPlace
    classes = ["collapse"]
    extra = 0
