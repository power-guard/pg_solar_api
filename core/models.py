"""
Creating the model to store the solar data.
"""
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    website_url = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        # Define unique constraint
        unique_together = [('name', 'email', 'phone_number')]

    def __str__(self):
        return self.name


class PowerPlant(models.Model):
    RESOURCE_CHOICES = [
        ('Solar', 'Solar'),
        ('Wind', 'Wind'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    ]
    
    plant_id = models.CharField(max_length=50)
    plant_name = models.CharField(max_length=100)
    resource = models.CharField(max_length=100, choices=RESOURCE_CHOICES, default='Solar')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    capacity_dc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    capacity_ac = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    utilities = models.ForeignKey('UtilitiesList', blank=True, null=True, on_delete=models.SET_NULL)
    companies = models.ManyToManyField('Company', blank=True)

    class Meta:
        # Define unique constraint based on plant_id, plant_name.
        unique_together = [('plant_id', 'plant_name')]

    def __str__(self):
        return self.plant_name


class LoggerCategory(models.Model):
    logger_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.logger_name


class Device(models.Model):
    device_id = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    #powerplant = models.ForeignKey(PowerPlant, on_delete=models.CASCADE)
    logger_name = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID {self.device_id} , Name {self.device_name}"

    class Meta:
            unique_together = [('device_id', 'device_name')]

class DevicePowerGen(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    logger_name = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)
    power_gen = models.DecimalField(max_digits=10, decimal_places=4)  # Accepts floating-point numbers with 4 digits after the decimal
    date = models.DateField(auto_now_add=True)  # Automatically sets the current date upon creation

    class Meta:
            unique_together = [('device_id', 'logger_name', 'date')]

class LoggerPowerGen(models.Model):
    logger_name = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)
    power_gen = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = [('logger_name', 'date')]


class CurtailmentEvent(models.Model):
    plant = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Curtailment Event for {self.plant.plant_name} on {self.date}"


"""
Utility data Model are created below this
"""

class UtilitiesList(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class UtilitiesCredential(models.Model):
    utility_name = models.ForeignKey(UtilitiesList, on_delete=models.CASCADE)
    website_link = models.URLField()
    website_id = models.CharField(max_length=100)
    website_pwd = models.CharField(max_length=100)

    class Meta:
        # Define unique constraint
        unique_together = [('utility_name', 'website_link', 'website_id')]


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



