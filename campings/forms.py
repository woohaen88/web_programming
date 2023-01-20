from django import forms
from django.utils.translation import gettext_lazy as _

from tags.models import Tag
from .models import Camping, CampingItem
from django.utils.text import slugify


class CampingCreateForm(forms.ModelForm):
    image = forms.FileField(
        label=_("캠핑장사진"),
        widget=forms.FileInput(attrs={"class": "form-control", "multiple": True}),
    )

    tags = forms.CharField(
        label=_("태그입력"),
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "태그1, 태그2, ... "}),
    )

    class Meta:
        model = Camping
        fields = (
            "title",
            "tags",
            "image",
            "content",
            "visited_dt",
            "address",  # 주소
            "site_url",  # 사이트주소
            "price",  # 가격
            "contact",  # 대표번호
            "is_car_charge",  # 충전여부
            "is_parking",  # 주차여부
            "is_add_car",  # 추가차량
            "is_add_human",  # 추가인원
        )

        labels = {
            "title": _("캠핑장이름"),
            "content": _("캠핑장리뷰"),
            "visited_dt": _("방문일자"),
            "address": _("주소"),  # 주소
            "site_url": _("사이트주소"),  # 사이트주소
            "price": _("가격"),  # 가격
            "contact": _("대표번호"),  # 대표번호
            "is_car_charge": _("충전여부"),  # 충전여부
            "is_parking": _("주차여부"),  # 주차여부
            "is_add_car": _("추가차량"),  # 추가차량
            "is_add_human": _("추가인원"),  # 추가인원
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder":"0000캠핑장"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder":"다음에 또가자!!"}),
            "visited_dt": forms.DateInput(attrs={"type": "date"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder":"캠핑장주소를 입력하세요"}),  # 주소
            "site_url": forms.TextInput(attrs={"class": "form-control", "placeholder":"캠핑장웹사이트 주소"}),  # 사이트주소
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder":"캠핑장주소 가격을 입력하세요"}),  # 가격
            "contact": forms.TextInput(attrs={"class": "form-control", "placeholder":"캠핑장전화번호를 입력하세요"}),  # 대표번호
            "is_car_charge": forms.Select(
                attrs={"class": "form-control", "type": "radio"}
            ),  # 충전여부
            "is_parking": forms.Select(
                attrs={"class": "form-control", "type": "radio"}
            ),  # 주차여부
            "is_add_car": forms.Select(
                attrs={"class": "form-control", "type": "radio"}
            ),  # 추가차량
            "is_add_human": forms.Select(
                attrs={"class": "form-control", "type": "radio"}
            ),  # 추가인원
        }

    def save(self, request, commit=True):
        instance = super().save(commit=False)
        instance.user_id = request.user.id

        # tag 입력
        tags = self.cleaned_data.get("tags")
        # tag1, tag3, tag5, tag2,   ,tag4

        tag_list = []
        new_tag_list = []
        for tag in tags.split(","):
            if len(tag) >= 1:
                tag = tag.strip()
                # 만약 tag가 Tag모델에 있으면 그대로
                if not Tag.objects.filter(name=tag).exists():
                    new_tag = Tag(name=tag, slug=slugify(tag, allow_unicode=True))
                    new_tag.save()
                    new_tag_list.append(tag)
                else:
                    tag_list.append(tag)
            # 없으면 Tag모델에 저장

        if commit:
            try:
                instance.save()
                for new_tag in new_tag_list:
                    tag_object = Tag.objects.get(name=new_tag)
                    instance.tag.add(tag_object)
                # TagList에서 하나씩 꺼내서 객체 만들기
                for exist_tag in tag_list:
                    tag_object = Tag.objects.get(name=exist_tag)
                    instance.tag.add(tag_object)
            except:
                pass
        return instance


class CampingUpdateForm(forms.ModelForm):
    # image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Camping
        fields = (
            "title",
            # "image",
            "content",
            "visited_dt",
        )


class CampingItemCreateForm(forms.ModelForm):
    class Meta:
        model = CampingItem
        fields = (
            "name",
            "price",
            "target_url",
        )

        labels = {
            "name": _("아이템이름"),
            "price": _("상품 가격"),
            "target_url": _("링크"),
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "상품이름"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "가격"}
            ),
            "target_url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "url"}
            ),
        }

    def save(self, request, commit=True):
        instance = super().save(commit=False)
        instance.user_id = request.user.id
        instance.target_url = instance.target_url.strip()

        is_ok = False
        while not is_ok:
            rand_string = self.Meta.model.rand_string()
            url_instance = self.Meta.model.objects.filter(shortened_url=rand_string)
            if not url_instance.exists():
                is_ok = True

        instance.shortened_url = rand_string
        if commit:
            try:
                instance.save()
            except Exception as e:
                pass

        return instance
