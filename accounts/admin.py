# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Custom admin interface for the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser

# Register CustomUser model with the custom admin interface
admin.site.register(CustomUser, CustomUserAdmin)
