<<<<<<< HEAD
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "role"]
    fieldsets = UserAdmin.fieldsets + (("Custom Fields", {"fields": ("role",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
=======
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "role"]
    fieldsets = UserAdmin.fieldsets + (("Custom Fields", {"fields": ("role",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
>>>>>>> 84cd1563f84fde80347479da1b81d5b66bc77fea
