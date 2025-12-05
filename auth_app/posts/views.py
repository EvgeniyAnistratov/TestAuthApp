from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from authorization.permissions import CreatePermission, ReadAllPermission, SpecificElementPermission

from .models import Post, Comment
from .serializers import PostSerializer, PostCommentSerializer


class PostListCreateView(ListCreateAPIView):
    permission_for_model = Post
    permission_classes = [ReadAllPermission, CreatePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostView(RetrieveUpdateDestroyAPIView):
    permission_classes = [SpecificElementPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCommentListView(APIView):
    permission_for_model = Comment
    permission_classes = [ReadAllPermission]

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post.objects.prefetch_related('comments'), id=pk)
        comments_data = PostCommentSerializer(post.comments.all(), many=True)
        return Response(comments_data.data)


class PostCommentView(RetrieveUpdateDestroyAPIView):
    permission_classes = [SpecificElementPermission]
    queryset = Comment.objects.all()
    serializer_class = PostCommentSerializer


class CreatePostCommentView(CreateAPIView):
    permission_for_model = Comment
    permission_classes = [CreatePermission]
    serializer_class = PostCommentSerializer
