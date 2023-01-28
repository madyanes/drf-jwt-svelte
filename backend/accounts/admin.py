from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'full_name', 'is_active')


admin.site.register(User, UserAdmin)
