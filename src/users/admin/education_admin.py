from django.contrib import admin

from ..models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    autocomplete_fields = [
        "user",
    ]
    list_display = ["user", "name", "date_start", "date_end"]
