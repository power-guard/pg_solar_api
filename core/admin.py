from django.contrib import admin
from . import models


"""
Admin view for Power plan details
"""
@admin.register(models.PowerPlantDetail)
class PowerPlantDetailAdmin(admin.ModelAdmin):
    list_display = ('system_name', 'system_id',  'country_name', 'latitude', 'longitude', 'azimuth', 'tilt', 'capacity_dc', 'created_at', 'updated_at','user')



"""
Admin view for solar power plan power generation
"""

@admin.register(models.LoggerCategory)
class LoggerCategoryAdmin(admin.ModelAdmin):
    list_display = ('logger_name', 'created_at', 'updated_at','user')

@admin.register(models.LoggerPowerGen)
class LoggerPowerGenAdmin(admin.ModelAdmin):
    list_display = ('logger_name', 'power_gen', 'date','status', 'created_at','updated_at','user')


@admin.register(models.CurtailmentEvent)
class CurtailmentEventAdmin(admin.ModelAdmin):
    list_display = ('plant', 'date', 'start_time', 'end_time','status',  'created_at', 'updated_at','user')


"""
Admin view for Utilitie detais
"""

@admin.register(models.UtilitieMonthlyRevenue)
class PlantMonthlyRevenueAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'contract_id', 'amount_kwh',
                    'amount_jpy', 'tax_jpy', 'period_year',
                    'period_month', 'rd','status',  'created_at', 'updated_at','user')

@admin.register(models.UtilitieMonthlyExpense)
class PlantMonthlyExpenseAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'contract_id', 'amount_kwh',
                    'amount_jpy', 'tax_jpy', 'period_year',
                    'period_month', 'rd','status',  'created_at', 'updated_at','user')

@admin.register(models.UtilitieDailyProduction)
class PlantMonthlyExpensesAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'amount_kwh', 'prod_date',
                    'period_year', 'period_month', 'rd','status',  'created_at', 'updated_at','user')

