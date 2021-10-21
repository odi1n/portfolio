from django.contrib import admin
from ..models import SocialType


@admin.register(SocialType)
class SocialTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']