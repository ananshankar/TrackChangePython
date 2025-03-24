"""
URL mappings for Labels app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from labels import views

router = DefaultRouter()
router.register('labels', views.LabelViewSet)

app_name = 'labels'
urlpatterns = [
    path('', include(router.urls))
]
