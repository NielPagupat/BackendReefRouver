from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('App.data.urls')),
    path('auth/', include('App.DeviceRequest.urls')),
]
