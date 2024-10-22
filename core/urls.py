from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Initialize DefaultRouter
router = DefaultRouter()

# Register ViewSets with the router
router.register(r'power-plant-detail', views.PowerPlantDetailViewSet, basename='power-plant-detail')
router.register(r'logger-power-gen', views.LoggerPowerGenViewSet, basename='logger-power-gen')
router.register(r'loggercategories', views.LoggerCategoryViewSet, basename='loggercategories')
router.register(r'curtailment-event', views.CurtailmentEventViewSet, basename='curtailment-event')

#loggers-plants-group Viewsets
router.register(r'loggers-plants-group', views.LoggerPlantGroupViewSet, basename='loggers-plants-group')

# Utility-related ViewSets
router.register(r'utlity-monthly-revenue', views.UtlityMonthlyRevenueViewSet, basename='utlity-monthly-revenue')
router.register(r'utlity-monthly-expense', views.UtlityMonthlyExpenseViewSet, basename='utlity-monthly-expense')
router.register(r'utlity-daily-production', views.UtlityDailyProductionViewSet, basename='utlity-daily-production')
router.register(r'utlity-plants-list', views.UtlityPlantIdViewSet, basename='utlity-plants-list')

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Register all ViewSet URLs
    #path('csrf-token-endpoint/', views.csrf_token_view, name='csrf_token'),  # CSRF token endpoint
]
