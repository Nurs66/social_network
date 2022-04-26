from django.db import models

from apps.users.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Title'
    )
    description = models.TextField(
        verbose_name='Description'
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} -- {self.post.title}"
