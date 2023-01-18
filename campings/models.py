from django.db import models
from django.urls import reverse
from django.conf import settings
from tags.models import Tag
import string
import random

class Camping(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="camping/%Y/%m/%d", blank=True)
    content = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    visited_dt = models.DateTimeField()

    # foreign key
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="camping",
    )

    # many to many field
    tag = models.ManyToManyField(Tag, related_name="camping")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-updated_dt",)

    def get_absolute_url(self):
        return reverse(
            "campings:detail",
            args=(self.pk,),
        )

    def get_update_url(self):
        return reverse(
            "campings:update",
            args=(self.pk,),
        )



class CampingItemCategory(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)

    def __str__(self):
        return self.name

class CampingItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="camping_items")
    camping_item_category = models.ForeignKey(CampingItemCategory, on_delete=models.SET_NULL, null=True, related_name="camping_items")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    target_url = models.URLField(max_length=2000)  # 입력 폼
    shortened_url = models.CharField(max_length=8, unique=True)  # 결과

    def rand_string():
        str_pool = string.ascii_letters + string.digits
        return ("".join([random.choice(str_pool) for i in range(8)])).lower()

    def __str__(self):
        return self.name

