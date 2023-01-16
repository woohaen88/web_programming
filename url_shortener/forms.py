from django import forms
from url_shortener.models import ShortenedUrls
from django.utils.translation import gettext_lazy as _

from web_programming.utils import url_count_changer


class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrls
        fields = ("nick_name", "target_url",)
        labels = {
            "nick_name": _("별칭"),
            "target_url": _("URL"),
        }
        widgets = {
            "nick_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL을 구분하기 위한 별칭"}),
            "target_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "포워딩될 URL"})
        }

    def save(self, request, commit=True):
        instance = super().save(commit=False)
        instance.creator_id = request.user.id
        instance.target_url = instance.target_url.strip()
        if commit:
            try:
                instance.save()
            except Exception as e:
                pass
            else:
                url_count_changer(request, True)

        return instance

    def update_form(self, request, url_id):
        instance = super().save(request, url_id, commit=False)
        instance.target_url = instance.target_url.strip()
        ShortenedUrls.objects.filter(pk=url_id, creator_id=request.user.id).update(
            target_url=instance.target_url,
            nick_name=instance.nick_name,
        )





