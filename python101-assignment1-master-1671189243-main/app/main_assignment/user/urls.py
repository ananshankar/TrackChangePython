"""
URL mappings for the User API
"""

from django.urls import path, include
from user import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register(
    'userprojectrelation',
    views.UserProjectRelationViewset,
    basename='userprojectrelation'
)

app_name = 'user'
urlpatterns = [
    path('login/', views.CreateUserView.as_view(), name='login'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]