"""
Creating the model to store the solar data.
"""
from django.db import models
from datetime import date

from django.conf import settings


"""
Power plan details 
"""


class PowerPlantDetail(models.Model):
    RESOURCE_CHOICES = [
        ('Solar', 'Solar'),
        ('Wind', 'Wind'),
    ]
    
    system_name = models.CharField(max_length=50)
    system_id = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    resource = models.CharField(max_length=100, choices=RESOURCE_CHOICES, default='Solar')
    country_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=15, decimal_places=12)
    longitude = models.DecimalField(max_digits=15, decimal_places=12)
    altitude = models.DecimalField(max_digits=10, decimal_places=4)
    azimuth = models.DecimalField(max_digits=10, decimal_places=4)
    tilt = models.DecimalField(max_digits=10, decimal_places=4)
    capacity_dc = models.DecimalField(max_digits=10, decimal_places=2)
    capacity_ac = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)

    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    
    
    class Meta:
        # Define unique constraint based on plant_id, plant_name.
        unique_together = [('system_name', 'system_id')]

    def __str__(self):
        return self.system_name



"""
Solar power plan detsils
"""


class LoggerCategory(models.Model):
    logger_name = models.CharField(max_length=100, unique=True)

    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.logger_name



class LoggerPowerGen(models.Model):
    logger_name = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)
    power_gen = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(null=True, blank=True, default=date.today)
    
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    
    class Meta:
        unique_together = [('logger_name', 'date')]


class CurtailmentEvent(models.Model):
    plant = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f"Curtailment Event for {self.plant.plant_name} on {self.date}"




"""
Utility data Model are created below this
"""
class UtilitieMonthlyRevenue(models.Model):
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
    
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    class Meta:
        # Define unique constraint based on plant_id, period_year, and period_month
        unique_together = [('plant_id', 'period_year', 'period_month')]


class UtilitieMonthlyExpense(models.Model):
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

    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    class Meta:
        # Define unique constraint based on plant_id, period_year, and period_month
        unique_together = [('plant_id', 'period_year', 'period_month')]


class UtilitieDailyProduction(models.Model):
    plant_id = models.CharField(max_length=50)
    amount_kwh = models.DecimalField(max_digits=10, decimal_places=2,
                                     blank=True, null=True)
    prod_date = models.CharField(max_length=50, blank=True, null=True)
    period_year = models.IntegerField(blank=True, null=True)
    period_month = models.IntegerField(blank=True, null=True)
    rd = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    class Meta:
        # Define unique constraint based on plant_id, period_year, and period_month
        unique_together = [('plant_id', 'prod_date')]



