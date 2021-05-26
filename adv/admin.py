from django.contrib import admin
from .models import MyClass, Employee
# Register your models here.
admin.site.register(MyClass)
admin.site.register(Employee)