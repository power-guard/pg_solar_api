from django.contrib import admin
from . import models


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
