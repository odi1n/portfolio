from django.contrib import admin
from ..models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    pass
