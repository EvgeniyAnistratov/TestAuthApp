from django.urls import path

from .views import ElementListView, PermissionView, PermissionListView, RoleListView

urlpatterns = [
    path('elements', ElementListView.as_view()),
    path('permissions', PermissionListView.as_view()),
    path('permissions/<int:pk>', PermissionView.as_view()),
    path('roles', RoleListView.as_view()),
]
