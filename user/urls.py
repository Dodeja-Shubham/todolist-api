from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:id>', views.User_Each_View.as_view()),
    path('registration/', include('rest_auth.registration.urls')),
]