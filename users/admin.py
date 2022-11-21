"""
Admin file for users app
"""
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseAdmin):
    """
    User admin interface
    """

    list_display = ["id", "__str__", "is_active", "gender"]
    list_display_links = ["id", "__str__"]
    list_filter = ["is_active", "is_staff", "is_superuser", "gender"]
    search_fields = ["first_name", "last_name", "email"]
    readonly_fields = ["uid", "created_at", "updated_at"]
    ordering = ["id"]
    fieldsets = [
        [None, {"fields": ["email", "password"]}],
        [
            "Info",
            {
                "fields": [
                    "uid",
                    "first_name",
                    "last_name",
                    "gender",
                    "profile_image",
                    "created_at",
                    "updated_at",
                ]
            },
        ],
        ["Flags", {"fields": ["is_active", "is_staff", "is_superuser"]}],
        ["Permissions", {"fields": ["groups", "user_permissions"]}],
    ]
