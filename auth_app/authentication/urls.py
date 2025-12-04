from django.urls import path

from .views import RegistrationView, LoginView, LogoutView, RefreshTokenView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('refresh', RefreshTokenView.as_view()),
    path('register', RegistrationView.as_view()),
]
