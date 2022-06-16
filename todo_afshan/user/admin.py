from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','is_staff','is_active']
    list_editable = ['is_staff']
    readonly_fields = ['username','password']