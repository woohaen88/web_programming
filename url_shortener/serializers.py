from rest_framework import serializers
from url_shortener.models import ShortenedUrls
from accounts.serializers import UserSerializer


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
