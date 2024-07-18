from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


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


# class DeviceViewSet(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     viewsets.GenericViewSet):
#     """View for managing Device API"""
#     serializer_class = serializers.DeviceSerializer
#     queryset = models.Device.objects.all()
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         data = request.data

#         # Extract logger_name from request data
#         logger_name_str = data.get('logger_name')

#         # Get or create LoggerCategory without updating existing records
#         logger_category, _ = models.LoggerCategory.objects.get_or_create(
#             logger_name=logger_name_str
#         )

#         # Update the request data to include the foreign key for logger_category
#         data['logger_name'] = logger_category.id

#         # Use the serializer to create the Device
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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

# class DevicePowerGenViewSet(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                             viewsets.GenericViewSet):
#     queryset = models.DevicePowerGen.objects.all()
#     serializer_class = serializers.DevicePowerGenSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

class LoggerPowerGenViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = models.LoggerPowerGen.objects.all()
    serializer_class = serializers.LoggerPowerGenSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]