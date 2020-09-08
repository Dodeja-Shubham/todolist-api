from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:id>', views.User_Each_View.as_view()),
    path('registration/', views.registration_view, name='register'),
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.UserLogout.as_view()),
]