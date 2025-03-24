"""
URL mappings for Sprint app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sprint import views

router = DefaultRouter()
router.register('sprint', views.SprintViewSet)

app_name = 'sprint'
urlpatterns = [
    path('', include(router.urls))
]
