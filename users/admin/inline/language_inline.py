from django.contrib import admin

from ...models import Language


class LanguageStackedInline(admin.StackedInline):
    model = Language
    classes = ['collapse']
    extra = 1
