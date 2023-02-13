from django.contrib import admin

from ..models import LanguageType


@admin.register(LanguageType)
class LanguageTypeAdmin(admin.ModelAdmin):
    search_fields = ["text"]
    list_filter = ["text"]
