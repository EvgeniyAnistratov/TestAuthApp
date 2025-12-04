from django.db import models

from auth_app.abstract_models import AbstractElement


class Post(AbstractElement):
    header = models.CharField(max_length=124)
    text = models.TextField()


class Comment(AbstractElement):
    comment = models.CharField(max_length=1024)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
