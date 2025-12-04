from django.db import models

from auth_app.abstract_models import AbstractElement


class Article(AbstractElement):
    header = models.CharField(max_length=124)
    text = models.TextField()


class Comment(AbstractElement):
    comment = models.CharField(max_length=1024)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
