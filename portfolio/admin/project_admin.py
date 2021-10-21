from django.contrib import admin
from ..models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['title']
    filter_horizontal = ['tech']
    list_display = ['title',
                    'link',
                    'description']
    list_filter = ['title']