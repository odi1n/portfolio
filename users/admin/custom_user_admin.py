from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = ['email',
                     'username', ]
    list_display = ['id',
                    'email',
                    'username',
                    'first_name', 'last_name',
                    'age',
                    'is_active',
                    'is_superuser',
                    'last_login',
                    'date_joined']
    list_display_links = ['id',
                          'email', ]
    filter_horizontal = ['groups',
                         'user_permissions']
    fieldsets = [
        (None, {
            'fields': ['username',
                       'email',
                       'password']
        }),
        [('Персональные данные'), {
            'fields': ['last_name',
                       'first_name',
                       'middle_name',
                       'sex',
                       'age', ],
        }],
        [('Доступ'), {
            'fields': ['is_active',
                       'is_staff',
                       'is_superuser',
                       'groups',
                       'user_permissions'],
        }],
        [('Время'), {
            'fields': ['last_login',
                       'date_joined']
        }],
    ]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    ordering = ('-date_joined',)
    search_fields = ['email',
                     'username',
                     'first name']
