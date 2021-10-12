from django.contrib import admin

# Register your models here.
from portfolio.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'description',
                    'updated_at',
                    'created_at']
    list_display_links = ['id',
                          'name']
