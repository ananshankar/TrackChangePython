"""
URL mappings for Watcher app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watcher import views

router = DefaultRouter()
router.register('watcher', views.WatcherViewSet)

app_name = 'watcher'
urlpatterns = [
    path('', include(router.urls))
]
