from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    updated_dt = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    url_count = models.IntegerField(default=0)

    follower_set = models.ManyToManyField("self", blank=True)
    following_set = models.ManyToManyField("self", blank=True)

    @property
    def name(self):
        return f"{self.email}"
