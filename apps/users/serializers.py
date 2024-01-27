from rest_framework import serializers

from .models import Author
from ..blog.models import Post


class AuthorTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('title', 'image', 'description', 'facebook_url', 'twitter_url', 'instagram_url')


class PostAuthorSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('post_count',)

    def get_post_count(self, obj):
        return obj.author.posts.count()


class AuthorSerializer(serializers.ModelSerializer):
    posts = PostAuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('title', 'image', 'posts')


class AuthorPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'title', 'image', 'description', 'content', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('title', 'image',)


class PostAuthorDetailSerializer(serializers.ModelSerializer):
    author = AuthorDetailSerializer()

    class Meta:
        model = Post
        fields = ('author', 'title', 'image', 'category', 'short_content', 'read_min', 'created_at',)
