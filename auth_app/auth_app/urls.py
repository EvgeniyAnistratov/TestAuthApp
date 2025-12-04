from django.urls import include, path

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('users/', include('users.urls')),
]
