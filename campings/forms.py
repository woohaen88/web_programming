from django import forms
from .models import Camping


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
