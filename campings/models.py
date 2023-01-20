import random
import string

from django.conf import settings
from django.db import models
from django.urls import reverse

from tags.models import Tag
from django.utils.translation import gettext_lazy as _
from django.utils import timezone



class Camping(models.Model):
    title = models.CharField(max_length=100)  # 캠핑장 이름
    content = models.TextField()  # 캠핑장 리뷰
    created_dt = models.DateTimeField(auto_now_add=True)  # 생성일자
    updated_dt = models.DateTimeField(auto_now=True)  # 수정일자
    visited_dt = models.DateTimeField(default=timezone.now)  # 방문일자
    address = models.CharField(max_length=255)
    site_url = models.URLField(blank=True)
    price = models.PositiveIntegerField()

    class IsCarCharge(models.TextChoices):  # 전기차 충전
        CAN = "1", _("충전가능")
        VAN = "2", _("충전불가")
        SEMI = "3", _("돈내면 가능")
        DONTKNOW = "4", _("모름")

    is_car_charge = models.CharField(
        max_length=10, choices=IsCarCharge.choices, default=IsCarCharge.DONTKNOW
    )

    class IsParking(models.TextChoices):  # 주차 가능
        CAN = "1", _("사이트옆 주차")
        VAN = "2", _("주차장 멀음")
        DONTKNOW = "3", _("모름")

    is_parking = models.CharField(
        max_length=10, choices=IsParking.choices, default=IsParking.DONTKNOW
    )

    contact = models.CharField(max_length=20)  # 전화번호

    class IsAddCar(models.TextChoices):  # 추가차량
        CAN = "1", _("가능")
        VAN = "2", _("불가")
        DONTKNOW = "3", _("모름")

    is_add_car = models.CharField(
        max_length=10, choices=IsAddCar.choices, default=IsAddCar.DONTKNOW
    )

    class IsAddHuman(models.TextChoices):  # 추가인원
        CAN = "1", _("가능")
        VAN = "2", _("불가")
        DONTKNOW = "3", _("모름")

    is_add_human = models.CharField(
        max_length=10, choices=IsAddHuman.choices, default=IsAddHuman.DONTKNOW
    )

    # foreign key
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="camping",
    )

    # many to many field
    tag = models.ManyToManyField(Tag, related_name="camping", blank=True)

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


class MultipleImage(models.Model):
    images = models.FileField(upload_to="images/camping/%Y/%m/%d")
    camping = models.ForeignKey(
        Camping, on_delete=models.CASCADE, related_name="multiple_image"
    )


class CampingItemCategory(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)

    def __str__(self):
        return self.name


class CampingItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="camping_items"
    )
    camping_item_category = models.ForeignKey(
        CampingItemCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="camping_items",
    )
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
