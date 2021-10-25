from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
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

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
