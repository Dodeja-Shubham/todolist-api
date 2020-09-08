from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Todolist API",
      default_version='v1',
      description="This is the REST API documentation for Todo List API\'s",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('todo/', include('todoitems.urls')),
    path('swagger/', schema_view.with_ui('swagger',
                                            cache_timeout=0), name='schema-swagger-ui'),
]
