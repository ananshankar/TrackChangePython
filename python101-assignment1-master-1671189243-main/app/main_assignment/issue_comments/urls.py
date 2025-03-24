"""
URL mappings for Comments app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from issue_comments import views

router = DefaultRouter()
router.register('issue_comments', views.CommentViewSet)

app_name = 'issue_comments'
urlpatterns = [
    path('', include(router.urls))
]
