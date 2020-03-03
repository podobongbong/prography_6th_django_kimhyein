from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Post


class PostSerializer(HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'author', 'created_at', 'description']
