from django.contrib import admin
from department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'supervisor', 'register_in', 'updated_in', 'activated',)
    list_display_links = ('id', 'department', 'supervisor', 'register_in', 'updated_in',)
    list_editable = ('activated',)
