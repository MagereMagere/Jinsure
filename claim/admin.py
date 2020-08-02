from django.contrib import admin

from .models import FileClaimVehicleTheft

# Register your models here.
@admin.register(FileClaimVehicleTheft)
class FileClaimVehicleTheftAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', 'occupation', 'phone_number', 'email']