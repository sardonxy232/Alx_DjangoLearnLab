# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                'role',
                'phone_number',
                'date_of_birth',
                'profile_photo',
            )
        }),
    )
    list_display = ['username', 'email', 'role', 'phone_number', 'date_of_birth', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)

