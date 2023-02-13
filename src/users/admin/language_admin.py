from django.contrib import admin
from ..models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['text']
    autocomplete_fields = ['user',
                           'language_type']
    list_display = ['user',
                    'language_type',
                    'text']
    list_filter = ['language_type__text',
                   'text']