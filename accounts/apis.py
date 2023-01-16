from rest_framework import viewsets
from url_shortener.models import ShortenedUrls
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
