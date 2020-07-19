from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Customer



@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ("customer", "item", "total", "quantity" ,"date")

