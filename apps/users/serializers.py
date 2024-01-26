from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'title', 'image', 'description', 'content', 'facebook_url', 'twitter_url', 'instagram_url',
                  'pinterest_url', 'is_top', 'created_at', 'updated_at')
