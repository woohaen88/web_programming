from rest_framework import permissions
from rest_framework import viewsets

from url_shortener.models import ShortenedUrls
from url_shortener.serializers import UrlListSerializer


class UrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = ShortenedUrls.objects.all()
    serializer_class = UrlListSerializer
    permission_classes = [permissions.IsAuthenticated]
