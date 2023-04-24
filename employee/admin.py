from django.contrib import admin
from employee.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'rut', 'phone', 'company']