
from django.contrib import admin

from .models import User, UserStatus

class UserAdmin(admin.ModelAdmin):
    fields = (
        'id', 'email', 'username',
        'is_active', 'is_staff', 'is_superuser', 
    )
    list_display = (
        'id', 'email', 'username',
        'is_active', 'is_staff', 'is_superuser', 
    )
    list_editable = (
        'is_active', 'is_staff', 'is_superuser',
    )
    search_fields = (
        'id', 'email', 
        'is_active', 'is_staff', 'is_superuser', 
    )
    readonly_fields = (
        'id',
    )

class UserStatusAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title', 
    )
    list_display = (
        'id', 'title',
    )
    list_editable = (
        'title',
    )
    search_fields = (
        'id', 'title',
    )
    readonly_fields = (
    )



admin.site.register(User, UserAdmin)
admin.site.register(UserStatus, UserStatusAdmin)