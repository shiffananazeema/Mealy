from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),  # Include Djoser URLs
    path('auth/', include('djoser.urls.jwt')),  # Include JWT endpoints
]
