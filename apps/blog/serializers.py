from rest_framework import serializers

from apps.blog.models import Category, Tag, Post
from apps.users.models import Author


class AuthorFeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('title', 'image',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class PostRecentlySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorFeaturedSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'title', 'author', 'category', 'image', 'short_content', 'read_min', 'created_at')


class PostPopularSerializer(serializers.ModelSerializer):
    author = AuthorFeaturedSerializer()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'title', 'author', 'category', 'short_content', 'read_min', 'created_at')


class PostFeaturedSerializer(serializers.ModelSerializer):
    author = AuthorFeaturedSerializer()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'title', 'author', 'category', 'short_content', 'read_min', 'created_at')


class SearchSerializer(serializers.ModelSerializer):
    author = AuthorFeaturedSerializer()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'short_content', 'read_min', 'created_at')


class CategoryWithImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'image', 'short_content', 'content', 'created_at')
