from django.contrib import admin
from ..models import Tech


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    search_fields = ['category',
                     'text']
    list_display = ['category',
                    'text']
    list_filter = ['category']