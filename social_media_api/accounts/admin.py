from django.contrib import admin

# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Profile", {"fields": ("bio", "profile_picture", "followers")}),
    )
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")
