from django.db import models
from django.urls import reverse
from django.conf import settings
from tags.models import Tag


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
