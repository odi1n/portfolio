from django.contrib import admin
from ..models import WorkPlace


@admin.register(WorkPlace)
class WorkPlaceAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        "user",
    ]
    list_display = ["user", "text"]
