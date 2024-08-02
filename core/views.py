from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
from .filters import LoggerPowerGenFilter


class CompanyViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """View for managing Company API"""
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UtilitiesListViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """View for managing UtilitiesList API"""
    serializer_class = serializers.UtilitiesListSerializer
    queryset = models.UtilitiesList.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UtilitiesCredentialViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """View for managing UtilitiesCredential API"""
    serializer_class = serializers.UtilitiesCredentialSerializer
    queryset = models.UtilitiesCredential.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Create a new utilities credential."""
        utilities_list, created = models.UtilitiesList.objects.get_or_create(
            name=serializer.validated_data['utility_name']
        )
        serializer.save(utility_name=utilities_list)


class PowerPlantViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """View for managing PowerPlant API"""
    serializer_class = serializers.PowerPlantSerializer
    queryset = models.PowerPlant.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class LoggerCategoryViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """View for managing LoggerCategory API"""
    serializer_class = serializers.LoggerCategorySerializer
    queryset = models.LoggerCategory.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PlantMonthlyRevenueViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    
    queryset = models.PlantMonthlyRevenue.objects.all()
    serializer_class = serializers.PlantMonthlyRevenueSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PlantMonthlyExpenseViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    
    queryset = models.PlantMonthlyExpense.objects.all()
    serializer_class = serializers.PlantMonthlyExpenseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PlantDailyProductionViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    
    queryset = models.PlantDailyProduction.objects.all()
    serializer_class = serializers.PlantDailyProductionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CurtailmentEventViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    
    queryset = models.CurtailmentEvent.objects.all()
    serializer_class = serializers.CurtailmentEventSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class LoggerPowerGenViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = models.LoggerPowerGen.objects.all()
    serializer_class = serializers.LoggerPowerGenSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LoggerPowerGenFilter