from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

"""
Power Plant Detail ViewSet URL
"""
router.register(r'power-plant-detail', views.PowerPlantDetailViewSet)

"""
Solare power generation URL
"""
router.register(r'logger-power-gen', views.LoggerPowerGenViewSet)
router.register(r'loggercategories', views.LoggerCategoryViewSet)
router.register(r'curtailment-event', views.CurtailmentEventViewSet)

"""
Utlity URL
"""
router.register(r'utlity-monthly-revenue', views.UtlityMonthlyRevenueViewSet)
router.register(r'utlity-monthly-expense', views.UtlityMonthlyExpenseViewSet)
router.register(r'utlity-daily-production', views.UtlityDailyProductionViewSet)
router.register(r'utlity-plants-list', views.UtlityPlantIdViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include all router URLs
    path('csrf-token-endpoint/', views.csrf_token_view, name='csrf_token'),  # CSRF token endpoint
]
