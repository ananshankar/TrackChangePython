from django.urls import path
from . import views

urlpatterns = [
    path('assignment1/question2/tests', views.CarsView.as_view({'get': 'get_test_cases_result'})),
    path('assignment1/question3/tests', views.StatesView.as_view({'get': 'get_test_cases_result'})),
    path('assignment1/question4/tests', views.FriendsView.as_view({'get': 'get_test_cases_result'})),
    path('assignment1/question1/tests', views.DataStructuresView.as_view({'get': 'get_test_cases_result'})),
    path('assignment2/question1/tests', views.ProfileView.as_view({'get': 'get_test_cases_result'})),
    path("api/login", views.TokenView.as_view()),
    path("api/user", views.UserView.as_view()),
    path("api/user/<id>", views.UserView.as_view())
]