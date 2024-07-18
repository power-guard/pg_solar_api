from django.contrib import admin
from . import models


admin.site.register(models.UtilitiesList)
admin.site.register(models.LoggerCategory)


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


# @admin.register(models.Device)
# class DeviceEventAdmin(admin.ModelAdmin):
#     list_display = ('logger_name', 'device_id', 'device_name')



@admin.register(models.PlantMonthlyRevenue)
class PlantMonthlyRevenueAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'contract_id', 'amount_kwh',
                    'amount_jpy', 'tax_jpy', 'period_year',
                    'period_month', 'rd')


@admin.register(models.PlantMonthlyExpense)
class PlantMonthlyExpenseAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'contract_id', 'amount_kwh',
                    'amount_jpy', 'tax_jpy', 'period_year',
                    'period_month', 'rd')


@admin.register(models.PlantDailyProduction)
class PlantMonthlyExpensesAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'amount_kwh', 'prod_date',
                    'period_year', 'period_month', 'rd')


@admin.register(models.CurtailmentEvent)
class CurtailmentEventAdmin(admin.ModelAdmin):
    list_display = ('plant', 'date', 'start_time', 'end_time')


# @admin.register(models.DevicePowerGen)
# class DevicePowerGenAdmin(admin.ModelAdmin):
#     list_display = ('logger_name', 'device_id', 'power_gen', 'date')

@admin.register(models.LoggerPowerGen)
class LoggerPowerGenAdmin(admin.ModelAdmin):
    list_display = ('logger_name', 'power_gen', 'date', 'created_at')
