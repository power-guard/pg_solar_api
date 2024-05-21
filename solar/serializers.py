"""
Serializers for solar APIs.
"""

from rest_framework import serializers
from .models import (
    Company,
    UtilitiesList,
    UtilitiesCredential,
    PowerPlant,
    LoggerCategory,
    Device
)


class CompanySerializer(serializers.ModelSerializer):
    """Serializers for Company"""

    class Meta:
        model = Company
        fields = ['id', 'name', 'address',
                  'website_url', 'email',
                  'phone_number', 'note']
        read_only_fiels = ['id']


class UtilitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilitiesList
        fields = ['id', 'name']
        read_only_fiels = ['id']


class UtilitiesCredentialSerializer(serializers.ModelSerializer):
    utility_name = serializers.CharField(write_only=True)
    utility_list = UtilitiesListSerializer(read_only=True)

    class Meta:
        model = UtilitiesCredential
        fields = ['id', 'utility_name', 'website_link',
                  'website_id', 'website_pwd', 'utility_list']
        read_only_fiels = ['id']

    def create(self, validated_data):
        utility_name = validated_data.pop('utility_name')
        # Get or create UtilitiesList instance
        utilities_list, created = UtilitiesList.objects.get_or_create(name=utility_name)
        # Check for duplicates before creating UtilitiesCredential
        if UtilitiesCredential.objects.filter(
                utility_name=utilities_list, 
                website_link=validated_data['website_link'],
                website_id=validated_data['website_id']
            ).exists():
            raise serializers.ValidationError("This credential already exists.")
        
        # Create the UtilitiesCredential instance
        utilities_credential = UtilitiesCredential.objects.create(
            utility_name=utilities_list,
            **validated_data
        )
        return utilities_credential

    def update(self, instance, validated_data):
        utility_name = validated_data.pop('utility_name', None)
        if utility_name:
            # Get or create UtilitiesList instance
            utilities_list, created = UtilitiesList.objects.get_or_create(name=utility_name)
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
        model = PowerPlant
        fields = ['id', 'plant_id', 'plant_name', 'resource', 'status',
                  'capacity_dc', 'capacity_ac', 'location', 'image',
                  'latitude', 'longitude', 'utilities', 'companies']
        read_only_fiels = ['id']

class LoggerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggerCategory
        fields = ['id', 'logger_name']
        read_only_fiels = ['id']


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['id', 'device_id', 'device_name', 'powerplant', 'logger_name']
        read_only_fiels = ['id']
