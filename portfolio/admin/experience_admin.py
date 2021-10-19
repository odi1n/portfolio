from django.contrib import admin
from ..models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass
