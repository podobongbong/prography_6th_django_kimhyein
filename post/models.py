from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(verbose_name='작성자', to=User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='게시물 제목', max_length=100)
    description = models.TextField(verbose_name='게시물 내용')
    created_at = models.DateTimeField(verbose_name='게시물 작성 시간', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
