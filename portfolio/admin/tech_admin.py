from django.contrib import admin
from ..models import Tech


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    pass
