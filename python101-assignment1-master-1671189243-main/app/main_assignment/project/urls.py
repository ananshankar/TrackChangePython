"""
URL mappings for Project app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project import views
from sprint import urls as sprint_urls

router = DefaultRouter()
router.register('project', views.ProjectViewSet)

app_name = 'project'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(sprint_urls)),
]
