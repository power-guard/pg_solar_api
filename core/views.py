from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from . import models
from . import serializers
from .filters import LoggerPowerGenFilter

"""
This is for CSRF toke.
"""
# from django.http import JsonResponse
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.middleware.csrf import get_token


"""
This is for CSRF toke.
"""
# @method_decorator(ensure_csrf_cookie, name='dispatch')
class BaseViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """Base viewset for utility models."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Automatically set the user to the authenticated user."""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """Automatically update the user during the update."""
        serializer.save(user=self.request.user)


class PowerPlantDetailViewSet(BaseViewSet):
    """View for managing PowerPlantDetail API"""
    serializer_class = serializers.PowerPlantDetailSerializer
    queryset = models.PowerPlantDetail.objects.all()


class LoggerCategoryViewSet(BaseViewSet):
    """View for managing LoggerCategory API"""
    serializer_class = serializers.LoggerCategorySerializer
    queryset = models.LoggerCategory.objects.all()


class LoggerPowerGenViewSet(BaseViewSet):
    """View for managing LoggerPowerGen API"""
    queryset = models.LoggerPowerGen.objects.all()
    serializer_class = serializers.LoggerPowerGenSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LoggerPowerGenFilter


class CurtailmentEventViewSet(BaseViewSet):
    """View for managing CurtailmentEvent API"""
    queryset = models.CurtailmentEvent.objects.all()
    serializer_class = serializers.CurtailmentEventSerializer



class UtlityPlantIdViewSet(BaseViewSet):
    """View for managing UtlityPlantId API"""
    queryset = models.UtlityPlantId.objects.all()
    serializer_class = serializers.UtilityPlantIdSerializer


class UtlityMonthlyRevenueViewSet(BaseViewSet):
    """View for managing UtilityMonthlyRevenue API"""
    queryset = models.UtilityMonthlyRevenue.objects.all()
    serializer_class = serializers.UtilityMonthlyRevenueSerializer


class UtlityMonthlyExpenseViewSet(BaseViewSet):
    """View for managing UtilitieMonthlyExpense API"""
    queryset = models.UtilityMonthlyExpense.objects.all()
    serializer_class = serializers.UtilityMonthlyExpenseSerializer


class UtlityDailyProductionViewSet(BaseViewSet):
    """View for managing UtilitieDailyProduction API"""
    queryset = models.UtilityDailyProduction.objects.all()
    serializer_class = serializers.UtilityDailyProductionSerializer








# @ensure_csrf_cookie
# def csrf_token_view(request):
#     """Returns the CSRF token for the client."""
#     return JsonResponse({'csrfToken': get_token(request)})