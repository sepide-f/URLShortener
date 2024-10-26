from rest_framework import serializers
from .models import URLShortener


class URLShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLShortener
        fields = ['id', 'url', 'short_code', 'created_at', 'updated_at']

    url = serializers.URLField()

