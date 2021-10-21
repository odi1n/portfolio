from django.contrib import admin
from ..models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    filter_horizontal = ['tech']
    list_display = ['id',
                    'user',
                    'stack']
    list_filter = ['stack']
    search_fields = ['user__username']