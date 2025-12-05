from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'header', 'text', 'owner']
        extra_kwargs = {'owner': {'read_only': True, 'required': False}}

    def save(self, **kwargs):
        self.validated_data['owner'] = self.context['request'].user
        return super().save(**kwargs)


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True, 'required': False}}

    def save(self, **kwargs):
        self.validated_data['owner'] = self.context['request'].user
        return super().save(**kwargs)
