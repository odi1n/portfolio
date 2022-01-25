from django.contrib import admin
from ..models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['portfolio',
                           'project']
    list_display = ['portfolio',
                    'project',
                    'description',
                    'is_enabled']
    fieldsets = (
        ('Настройки', {
            'fields': ('portfolio', 'project', 'description', 'is_enabled')
        }),
        ('Дата работы над проектом', {
            'classes': ('collapse',),
            'fields': (('started', 'completed'),),
        }),
    )
