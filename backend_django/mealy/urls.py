from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # This already includes a trailing slash
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('mealy_backend.urls')),
]
