from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Unregister the default User admin
admin.site.unregister(User)

# Create a new UserAdmin class to add 'id' to list_display
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('username', 'email', 'first_name', 'last_name')