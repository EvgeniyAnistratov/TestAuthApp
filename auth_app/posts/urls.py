from django.urls import path

from .views import PostListCreateView, PostView, PostCommentListView, PostCommentView, CreatePostCommentView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('/<int:pk>', PostView.as_view()),
    path('/<int:pk>/comments', PostCommentListView.as_view()),
    path('/comments', CreatePostCommentView.as_view()),
    path('/comments/<int:pk>', PostCommentView.as_view()),
]
