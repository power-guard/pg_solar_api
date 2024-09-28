"""
Serializers for solar APIs.
"""

from rest_framework import serializers
from . import models



"""
serializers for PowerPlantDetail
"""
class PowerPlantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerPlantDetail
        fields = '__all__'
        read_only_fields = ['user']



"""
serializers for solar power plan
"""

class LoggerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoggerCategory
        fields = '__all__'
        read_only_fiels = ['id']


class LoggerPowerGenSerializer(serializers.ModelSerializer):
    logger_name = serializers.CharField(source='logger_name.logger_name')  # Use the logger_name field from LoggerCategory
    user = serializers.StringRelatedField()

    class Meta:
        model = models.LoggerPowerGen
        fields = ['id','logger_name', 'power_gen', 'date', 'status', 'created_at', 'updated_at', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        logger_name_data = validated_data.pop('logger_name')
        logger_name, created = models.LoggerCategory.objects.get_or_create(logger_name=logger_name_data['logger_name'])
        validated_data['logger_name'] = logger_name
        return models.LoggerPowerGen.objects.create(**validated_data)


class CurtailmentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CurtailmentEvent
        fields = '__all__'



"""
serializers for Utilitie
"""

class UtilitieMonthlyRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UtilitieMonthlyRevenue
        fields = '__all__'

class UtilitieMonthlyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UtilitieMonthlyExpense
        fields = '__all__'

class UtilitieDailyProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UtilitieDailyProduction
        fields = '__all__'







