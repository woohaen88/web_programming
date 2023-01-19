import random
import string

from django.conf import settings
from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ShortenedUrls(models.Model):
    class Meta:
        ordering = ("-updated_at",)

    class CreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"

    def rand_string():
        str_pool = string.digits + string.ascii_letters
        rand_str = ("".join([random.choice(str_pool) for _ in range(6)])).lower()
        return rand_str

    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Categories,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="shortened_urls",
    )
    prefix = models.CharField(max_length=50)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shortened_urls",
    )
    target_url = models.URLField(max_length=2000)  # 입력 폼
    shortened_url = models.CharField(max_length=6, default=rand_string)  # 결과
    create_via = models.CharField(
        max_length=8, choices=CreatedVia.choices, default=CreatedVia.WEBSITE
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_update_url(self):
        return reverse("url_shortener:update", args=(self.pk,))

    def get_delete_url(self):
        return reverse("url_shortener:delete", args=(self.pk,))
