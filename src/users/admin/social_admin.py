from django.contrib import admin
from ..models import Social


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user", "social_type"]
    list_display = ["user", "social_type", "values"]
    list_filter = ["social_type"]
