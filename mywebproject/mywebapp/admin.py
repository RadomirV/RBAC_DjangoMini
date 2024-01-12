# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "role"]
    fieldsets = UserAdmin.fieldsets + (("Custom Fields", {"fields": ("role",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
