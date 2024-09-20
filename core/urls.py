from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

"""
Solare power generation URL
"""
router.register(r'logger-power-gen', views.LoggerPowerGenViewSet)
router.register('loggercategories', views.LoggerCategoryViewSet)
router.register(r'curtailment-event', views.CurtailmentEventViewSet)

"""
Utilitie URL
"""
router.register(r'utilitie-monthly-revenue', views.UtilitieMonthlyRevenueViewSet)
router.register(r'utilitie-monthly-expense', views.UtilitieMonthlyExpenseViewSet)
router.register(r'utilitie-daily-production', views.UtilitieDailyProductionViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
