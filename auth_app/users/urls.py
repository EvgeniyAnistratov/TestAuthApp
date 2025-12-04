from django.urls import path

from .views import GenericUserView

urlpatterns = [
    path('<int:pk>', GenericUserView.as_view()),
]
