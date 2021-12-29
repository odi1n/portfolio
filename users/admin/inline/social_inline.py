from django.contrib import admin

from ...models import Social


class SocialStackedInline(admin.StackedInline):
    model = Social
    classes = ['collapse']
    extra = 0
