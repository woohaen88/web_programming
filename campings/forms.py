from django import forms
from .models import Camping, CampingItem
from django.utils.translation import gettext_lazy as _


class CampingCreateForm(forms.ModelForm):
    title = forms.CharField()
    image = forms.ImageField(widget=forms.FileInput(attrs={"type": "file"}))
    content = forms.CharField(widget=forms.Textarea())
    visited_dt = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "date"}))

    class Meta:
        model = Camping
        fields = (
            "title",
            "image",
            "content",
            "visited_dt",
        )


class CampingUpdateForm(forms.ModelForm):
    # image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Camping
        fields = (
            "title",
            "image",
            "content",
            "visited_dt",
        )


class CampingItemCreateForm(forms.ModelForm):
    class Meta:
        model = CampingItem
        fields = ("name", "price", "target_url",)


        labels = {
            "name" : _("아이템이름"),
            "price" : _("상품 가격"),
            "target_url": _("링크"),
        }

        widgets = {
            "name" : forms.TextInput(attrs={"class":"form-control", "placeholder": "상품이름"}),
            "price" : forms.NumberInput(attrs={"class":"form-control", "placeholder": "가격"}),
            "target_url":forms.TextInput(attrs={"class":"form-control", "placeholder": "url"}),
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

