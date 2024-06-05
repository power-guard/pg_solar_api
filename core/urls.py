from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('utilities', views.UtilitiesListViewSet)
router.register('credentials', views.UtilitiesCredentialViewSet)
router.register('powerplants', views.PowerPlantViewSet)
router.register('loggercategories', views.LoggerCategoryViewSet)
router.register('devices', views.DeviceViewSet)
router.register(r'plant-monthly-revenue', views.PlantMonthlyRevenueViewSet)
router.register(r'plant-monthly-expense', views.PlantMonthlyExpenseViewSet)
router.register(r'plant-daily-production', views.PlantDailyProductionViewSet)
router.register(r'curtailment-event', views.CurtailmentEventViewSet)
router.register(r'device-power-gen', views.DevicePowerGenViewSet)
router.register(r'logger-power-gen', views.LoggerPowerGenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
