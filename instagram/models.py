from django.db import models
from django.conf import settings
import re

from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="image/%Y/%m/%d")
    caption = models.CharField(max_length=500)
    tag_set = models.ManyToManyField("Tag", blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def author_name(self):
    #     return f"{self.author.email}"

    class Meta:
        ordering = ("-updated_at",)

    def __str__(self):
        return self.caption

    def extract_tag_list(self):
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.caption)
        tag_list = []
        for tag_name in tag_name_list:
            if not Tag.objects.filter(name=tag_name).exists():
                tag, _ = Tag.objects.get_or_create(
                    name=tag_name, slug=slugify(tag_name, allow_unicode=True)
                )
                tag_list.append(tag)
        return tag_list

    def get_absolute_url(self):
        return reverse(
            "instagram:post_detail",
            kwargs={
                "post_pk": self.pk,
            },
        )
