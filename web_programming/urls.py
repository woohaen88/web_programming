from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.urls import router as user_router
from url_shortener.urls import router as url_router
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("accounts.urls")),
    path("camping/", include("campings.urls")),
    path("short/", include("url_shortener.urls")),
    path("tag/", include("tags.urls")),
    path("api/", include(user_router.urls)),
    path("api/", include(url_router.urls)),
    path("", views.IndexView.as_view(), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
