"""
Crating the model for utility company data store.
"""
from django.db import models
from solar.models import LoggerCategory


class PlantMonthlyRevenue(models.Model):
    plant_id = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=50, blank=True, null=True)
    amount_kwh = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True)
    amount_jpy = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True)
    tax_jpy = models.DecimalField(max_digits=10, decimal_places=2,
                                  blank=True, null=True)
    period_year = models.IntegerField(blank=True, null=True)
    period_month = models.IntegerField(blank=True, null=True)
    rd = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        # Define unique constraint based on plant_id, period_year, and period_month
        unique_together = [('plant_id', 'period_year', 'period_month')]


class PlantMonthlyExpense(models.Model):
    plant_id = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=50, blank=True, null=True)
    amount_kwh = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True)
    amount_jpy = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True)
    tax_jpy = models.DecimalField(max_digits=10, decimal_places=2,
                                  blank=True, null=True)
    period_year = models.IntegerField(blank=True, null=True)
    period_month = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=50, blank=True, null=True)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    rd = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        # Define unique constraint based on plant_id, period_year, and period_month
        unique_together = [('plant_id', 'period_year', 'period_month')]


class PlantDailyProduction(models.Model):
    plant_id = models.CharField(max_length=50)
    amount_kwh = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True)
    prod_date = models.CharField(max_length=50, blank=True, null=True)
    period_year = models.IntegerField(blank=True, null=True)
    period_month = models.IntegerField(blank=True, null=True)
    rd = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        # Define unique constraint based on plant_id, period_year, and period_month
        unique_together = [('plant_id', 'prod_date')]


class CurtailmentEvent(models.Model):
    plant = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Curtailment Event for {self.plant.plant_name} on {self.date}"
