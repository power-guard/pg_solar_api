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

    def __str__(self):
        return self.name


class UtilitiesList(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class UtilitiesCredential(models.Model):
    utility_name = models.ForeignKey(UtilitiesList, on_delete=models.CASCADE)
    website_link = models.URLField()
    website_id = models.CharField(max_length=100)
    website_pwd = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.utility_list} - {self.website_id}"


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
    resource = models.CharField(max_length=100,
                                choices=RESOURCE_CHOICES,
                                default='Solar')
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='active')
    capacity_dc = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True, null=True)
    capacity_ac = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True, null=True)
    location = models.CharField(max_length=255,
                                blank=True, null=True)
    image = models.ImageField(upload_to='plant_images/',
                              blank=True, null=True)
    latitude = models.DecimalField(max_digits=9,
                                   decimal_places=6, blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=9,
                                    decimal_places=6, blank=True,
                                    null=True)
    utilities = models.ForeignKey(UtilitiesList,
                                  blank=True, null=True,
                                  on_delete=models.SET_NULL)
    companies = models.ManyToManyField(Company)

    def __str__(self):
        return self.plant_name


class LoggerCategory(models.Model):
    logger_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    device_name = models.CharField(max_length=100)
    powerplant = models.ForeignKey(PowerPlant, on_delete=models.CASCADE)
    logger_name = models.ForeignKey(LoggerCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
