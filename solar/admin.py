from django.contrib import admin
from . import models


admin.site.register(models.UtilitiesList)


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website_url', 'email', 'phone_number', 'note')


@admin.register(models.UtilitiesCredential)
class UtilitiesCredentialAdmin(admin.ModelAdmin):
    list_display = ('utility_name', 'website_link', 'website_id')


@admin.register(models.PowerPlant)
class PowerPlantAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'plant_name',
                    'resource', 'capacity_dc', 'capacity_ac',
                    'utilities')


@admin.register(models.Device)
class CurtailmentEventAdmin(admin.ModelAdmin):
    list_display = ('logger_name', 'device_id', 'device_name', 'powerplant')
