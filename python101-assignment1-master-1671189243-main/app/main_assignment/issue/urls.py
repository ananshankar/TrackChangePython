"""
URL mappings for Issue app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from issue import views

router = DefaultRouter()
router.register('issues', views.IssueViewSet)

app_name = 'issue'
urlpatterns = [
    path('', include(router.urls))
]
