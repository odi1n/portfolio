from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django_json_widget.widgets import JSONEditorWidget
from .inline import *
from ..models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user"]
    filter_horizontal = ["tech"]
    list_display = [
        "id",
        "name",
        "user",
        "stack",
        "experience_with",
        "generate_pdf_preview_html",
    ]
    list_filter = ["stack", "experience_with"]
    list_display_links = ["id", "name", "user"]
    inlines = [WorkStackedInline, ExperienceStackedInline]
    search_fields = ["user__username"]
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }

    def generate_pdf_preview_html(self, obj):
        return format_html(
            '<a class="button" href="/portfolio/%s" target="_blank">Открыть портфолио</a>'
            % obj.id
        )

    generate_pdf_preview_html.short_description = "Портфолио"
    generate_pdf_preview_html.allow_tags = True
