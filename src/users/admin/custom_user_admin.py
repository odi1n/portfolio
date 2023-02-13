from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import CustomUser
from .inline import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ["email", "username", "first_name", "last_name"]
    list_display = [
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "age",
        "is_active",
        "is_superuser",
        "last_career_meeting",
        "last_login",
        "date_joined",
    ]
    list_filter = ["is_staff", "is_active", "is_superuser", "last_career_meeting"]
    list_display_links = ["id", "email", "username"]
    filter_horizontal = ["groups", "user_permissions"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (("Работа"), {"fields": ["last_career_meeting"]}),
        [
            ("Персональные данные"),
            {
                "fields": (
                    (
                        "last_name",
                        "first_name",
                        "middle_name",
                    ),
                    "sex",
                    "age",
                ),
            },
        ],
        [
            ("Доступ"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ],
            },
        ],
        [("Время"), {"fields": (("last_login", "date_joined"),)}],
    ]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    inlines = [
        LanguageStackedInline,
        SocialStackedInline,
        WorkPlaceStackedInline,
        EducationStackedInline,
    ]
    ordering = ("-date_joined",)
