from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = Post
        fields = ["title", "content", "date_posted", "author"]