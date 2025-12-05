from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from authorization.permissions import CreatePermission, ReadAllPermission, SpecificElementPermission

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleCommentSerializer


class ArticleListCreateView(ListCreateAPIView):
    permission_for_model = Article
    permission_classes = [ReadAllPermission, CreatePermission]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleView(RetrieveUpdateDestroyAPIView):
    permission_classes = [SpecificElementPermission]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCommentListView(APIView):
    permission_for_model = Comment
    permission_classes = [ReadAllPermission]

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Article.objects.prefetch_related('comments'), id=pk)
        comments_data = ArticleCommentSerializer(post.comments.all(), many=True)
        return Response(comments_data.data)


class ArticleCommentView(RetrieveUpdateDestroyAPIView):
    permission_classes = [SpecificElementPermission]
    queryset = Comment.objects.all()
    serializer_class = ArticleCommentSerializer


class CreateArticleCommentView(CreateAPIView):
    permission_for_model = Comment
    permission_classes = [CreatePermission]
    serializer_class = ArticleCommentSerializer
