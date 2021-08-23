from rest_framework import serializers
from HackerNews.apphn.models import Post


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'creator', 'created_on', 'url', 'description', 'votes', 'comments']
