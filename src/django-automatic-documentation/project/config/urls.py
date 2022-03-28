from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('test_app.urls')),
    path('docs/', include('config.yasg')),
]
