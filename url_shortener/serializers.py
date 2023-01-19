from rest_framework import serializers

from accounts.serializers import UserSerializer
from url_shortener.models import ShortenedUrls


class UrlListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = ShortenedUrls
        fields = [
            "id",
            "nick_name",
            "shortened_url",
            "creator",
            "create_via",
        ]
