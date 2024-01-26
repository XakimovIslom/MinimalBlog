from rest_framework import serializers

from apps.contact.models import ContactUsRequest, ContactUs


class ContactUsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsRequest
        fields = ('id', 'name', 'email', 'subject', 'text', 'created_at', 'updated_at')


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id', 'content', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url', 'created_at',
            'updated_at')
