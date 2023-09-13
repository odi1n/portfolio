from django.contrib import admin

from ..models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = [
        "portfolio",
        "grade",
        "salary",
        "post",
        "travel_time",
        "employment",
        "schedule",
    ]
    autocomplete_fields = ["portfolio"]
