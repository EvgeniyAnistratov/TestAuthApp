from rest_framework import serializers

from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'header', 'text', 'owner']
        extra_kwargs = {'owner': {'read_only': True, 'required': False}}

    def save(self, **kwargs):
        self.validated_data['owner'] = self.context['request'].user
        return super().save(**kwargs)


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True, 'required': False}}

    def save(self, **kwargs):
        self.validated_data['owner'] = self.context['request'].user
        return super().save(**kwargs)


class UpdateArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True, 'required': False},
            'created_at': {'read_only': True, 'required': False},
            'edited_at': {'read_only': True, 'required': False},
            'post': {'read_only': True, 'required': False},
        }

    def save(self, **kwargs):
        return super().save(**kwargs)
