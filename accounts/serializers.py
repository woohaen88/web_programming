from django.contrib.auth import get_user_model
from rest_framework import serializers
from url_shortener.models import ShortenedUrls


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ("password",)
