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