from django.urls import path

from .views import GenericUserView, UserAddRolesView, UserDeleteRolesView

urlpatterns = [
    path('<int:pk>', GenericUserView.as_view()),
    path('<int:pk>/add-roles', UserAddRolesView.as_view()),
    path('<int:pk>/delete-roles', UserDeleteRolesView.as_view()),
]
