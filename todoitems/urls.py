from django.urls import path, include
from todoitems import views

urlpatterns = [
    path('', views.ToDoItemView.as_view()),
    path('<int:id>', views.ToDoItem_Each_View.as_view())
]