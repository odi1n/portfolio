from django.contrib import admin

from ...models import Work


class WorkStackedInline(admin.StackedInline):
    model = Work
    classes = ['collapse']
    extra = 1
