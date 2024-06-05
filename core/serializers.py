"""
Serializers for solar APIs.
"""

from rest_framework import serializers
from . import models


class CompanySerializer(serializers.ModelSerializer):
    """Serializers for Company"""

    class Meta:
        model = models.Company
        fields = ['id', 'name', 'address',
                  'website_url', 'email',
                  'phone_number', 'note']
        read_only_fiels = ['id']


class UtilitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UtilitiesList
        fields = ['id', 'name']
        read_only_fiels = ['id']


class UtilitiesCredentialSerializer(serializers.ModelSerializer):
    utility_name = serializers.CharField(write_only=True)
    utility_list = UtilitiesListSerializer(read_only=True)

    class Meta:
        model = models.UtilitiesCredential
        fields = ['id', 'utility_name', 'website_link',
                  'website_id', 'website_pwd', 'utility_list']
        read_only_fiels = ['id']

    def create(self, validated_data):
        utility_name = validated_data.pop('utility_name')
        # Get or create UtilitiesList instance
        utilities_list, created = models.UtilitiesList.objects.get_or_create(name=utility_name)
        
        # Create the UtilitiesCredential instance
        utilities_credential = models.UtilitiesCredential.objects.create(
            utility_name=utilities_list,
            **validated_data
        )
        return utilities_credential

    def update(self, instance, validated_data):
        utility_name = validated_data.pop('utility_name', None)
        if utility_name:
            # Get or create UtilitiesList instance
            utilities_list, created = models.UtilitiesList.objects.get_or_create(name=utility_name)
            instance.utility_name = utilities_list

        instance.website_link = validated_data.get('website_link', instance.website_link)
        instance.website_id = validated_data.get('website_id', instance.website_id)
        instance.website_pwd = validated_data.get('website_pwd', instance.website_pwd)
        # Save the updated UtilitiesCredential instance
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['utility_name'] = instance.utility_name.name
        return representation


class PowerPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerPlant
        fields = ['id', 'plant_id', 'plant_name', 'resource', 'status',
                  'capacity_dc', 'capacity_ac', 'location', 'image',
                  'latitude', 'longitude', 'utilities', 'companies']
        read_only_fiels = ['id']

class LoggerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoggerCategory
        fields = ['id', 'logger_name']
        read_only_fiels = ['id']


class LoggerPowerGenSerializer(serializers.ModelSerializer):
    logger_name = serializers.CharField(source='logger_name.logger_name')  # Use the logger_name field from LoggerCategory

    class Meta:
        model = models.LoggerPowerGen
        fields = ['id', 'logger_name', 'power_gen', 'date']
        read_only_fields = ['id']

    def create(self, validated_data):
        logger_name_data = validated_data.pop('logger_name')
        logger_name, created = models.LoggerCategory.objects.get_or_create(logger_name=logger_name_data['logger_name'])
        validated_data['logger_name'] = logger_name
        return models.LoggerPowerGen.objects.create(**validated_data)


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = ['id', 'device_id', 'device_name', 'logger_name']
        read_only_fiels = ['id']



class PlantMonthlyRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlantMonthlyRevenue
        fields = '__all__'

class PlantMonthlyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlantMonthlyExpense
        fields = '__all__'

class PlantDailyProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlantDailyProduction
        fields = '__all__'

class CurtailmentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CurtailmentEvent
        fields = '__all__'

class DevicePowerGenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DevicePowerGen
        fields = '__all__'
