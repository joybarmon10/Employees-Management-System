from django.contrib import admin
from .models import Employees
# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone', 'salary', 'designation')
    search_fields = ('name', 'email', 'address', 'phone', 'salary', 'designation')

admin.site.register(Employees, EmployeesAdmin)
