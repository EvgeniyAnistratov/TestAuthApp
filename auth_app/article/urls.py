from django.urls import path

from .views import ArticleListCreateView, ArticleView, ArticleCommentListView, ArticleCommentView, CreateArticleCommentView

urlpatterns = [
    path('', ArticleListCreateView.as_view()),
    path('/<int:pk>', ArticleView.as_view()),
    path('/<int:pk>/comments', ArticleCommentListView.as_view()),
    path('/comments', CreateArticleCommentView.as_view()),
    path('/comments/<int:pk>', ArticleCommentView.as_view()),
]
