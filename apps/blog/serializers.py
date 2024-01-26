from rest_framework import serializers

from apps.blog.models import Category, Tag, Post
from apps.users.serializers import AuthorSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'created_at', 'updated_at', 'count')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    tag = serializers.SerializerMethodField(read_only=True, required=False)

    def get_tag(self, obj):
        tag = obj.tag.all()
        data = []
        for i in tag:
            data.append({'id': i.id, 'title': i.title})
        return data

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'title', 'category', 'image', 'short_content', 'content', 'read_min', 'tag', 'is_featured',
            'is_popular', 'created_at', 'updated_at')
