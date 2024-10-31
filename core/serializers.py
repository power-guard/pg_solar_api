from rest_framework import serializers
from . import models


"""
serializers for PowerPlantDetail
"""
class PowerPlantDetailSerializer(serializers.ModelSerializer):
    """Serializer for PowerPlantDetail."""
    class Meta:
        model = models.PowerPlantDetail
        fields = '__all__'
        read_only_fields = ['user']


"""
serializers for logger and plant group
"""
class LoggerPlantGroupSerializer(serializers.ModelSerializer):
    """Serializer for PowerPlantDetail."""
    class Meta:
        model = models.LoggerPlantGroup
        fields = '__all__'
        read_only_fields = ['user']




"""
serializers for solar power plan
"""
class LoggerCategorySerializer(serializers.ModelSerializer):
    """Serializer for LoggerCategory."""
    class Meta:
        model = models.LoggerCategory
        fields = '__all__'
        read_only_fields = ['id']


class LoggerPowerGenSerializer(serializers.ModelSerializer):
    """Serializer for LoggerPowerGen."""
    logger_name = serializers.CharField(source='logger_name.logger_name')  # Use the logger_name field from LoggerCategory
    user = serializers.StringRelatedField()

    class Meta:
        model = models.LoggerPowerGen
        fields = ['id', 'logger_name', 'power_gen', 'date', 'status', 'created_at', 'updated_at', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        logger_name_data = validated_data.pop('logger_name')
        logger_name, created = models.LoggerCategory.objects.get_or_create(logger_name=logger_name_data['logger_name'])
        validated_data['logger_name'] = logger_name
        return models.LoggerPowerGen.objects.create(**validated_data)


class CurtailmentEventSerializer(serializers.ModelSerializer):
    """Serializer for CurtailmentEvent."""
    user = serializers.StringRelatedField()

    class Meta:
        model = models.CurtailmentEvent
        fields = '__all__'
        read_only_fields = ['id']


"""
serializers for Utilitie
"""
class UtilityPlantIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UtilityPlantId
        fields = '__all__'
        read_only_fields = ['id']


class UtilityMonthlyRevenueSerializer(serializers.ModelSerializer):
    """Serializer for UtilityMonthlyRevenue."""
    plant_id = serializers.CharField(source='plant_id.plant_id')
    user = serializers.StringRelatedField()

    class Meta:
        model = models.UtilityMonthlyRevenue
        fields = [
            'id', 'plant_id', 'contract_id', 'start_date', 'end_date',
            'power_capacity_kw', 'sales_days', 'sales_electricity_kwh',
            'sales_amount_jpy', 'tax_jpy', 'average_daily_sales_kwh', 'rd', 'status',
            'user', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        plant_id_data = validated_data.pop('plant_id')
        plant_id, created = models.UtilityPlantId.objects.get_or_create(plant_id=plant_id_data['plant_id'])
        validated_data['plant_id'] = plant_id
        return models.UtilityMonthlyRevenue.objects.create(**validated_data)


class UtilityMonthlyExpenseSerializer(serializers.ModelSerializer):
    """Serializer for UtilityMonthlyExpense."""
    plant_id = serializers.CharField(source='plant_id.plant_id')
    user = serializers.StringRelatedField()

    class Meta:
        model = models.UtilityMonthlyExpense
        fields = [
            'id', 'plant_id', 'used_electricity_kwh', 'used_amount_jpy', 'tax_jpy',
            'rd', 'status', 'user', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        plant_id_data = validated_data.pop('plant_id')
        plant_id, created = models.UtilityPlantId.objects.get_or_create(plant_id=plant_id_data['plant_id'])
        validated_data['plant_id'] = plant_id
        return models.UtilityMonthlyExpense.objects.create(**validated_data)


class UtilityDailyProductionSerializer(serializers.ModelSerializer):
    """Serializer for UtilityDailyProduction."""
    plant_id = serializers.CharField(source='plant_id.plant_id')
    user = serializers.StringRelatedField()

    class Meta:
        model = models.UtilityDailyProduction
        fields = [
            'id', 'plant_id', 'power_production_kwh', 'production_date',
            'rd', 'status', 'user', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        plant_id_data = validated_data.pop('plant_id')
        plant_id, created = models.UtilityPlantId.objects.get_or_create(plant_id=plant_id_data['plant_id'])
        validated_data['plant_id'] = plant_id
        return models.UtilityDailyProduction.objects.create(**validated_data)
