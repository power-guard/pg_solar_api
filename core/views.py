from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
from .filters import LoggerPowerGenFilter



"""
View set for Plan power detais.
"""

class PowerPlantDetailViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """View for managing LoggerCategory API"""
    serializer_class = serializers.PowerPlantDetailSerializer
    queryset = models.PowerPlantDetail.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



"""
View set for Plan power generation and the envent.
"""

class LoggerCategoryViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """View for managing LoggerCategory API"""
    serializer_class = serializers.LoggerCategorySerializer
    queryset = models.LoggerCategory.objects.all()
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
                            mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = models.LoggerPowerGen.objects.all()
    serializer_class = serializers.LoggerPowerGenSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LoggerPowerGenFilter


"""
View set for Utilitie
"""

class UtilitieMonthlyRevenueViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    
    queryset = models.UtilitieMonthlyRevenue.objects.all()
    serializer_class = serializers.UtilitieMonthlyRevenueSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UtilitieMonthlyExpenseViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    
    queryset = models.UtilitieMonthlyExpense.objects.all()
    serializer_class = serializers.UtilitieMonthlyExpenseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UtilitieDailyProductionViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    
    queryset = models.UtilitieDailyProduction.objects.all()
    serializer_class = serializers.UtilitieDailyProductionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]