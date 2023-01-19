from django import forms
from django.utils.text import slugify

from tags.models import Tag


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)

    def save(self, commit=True):
        tag = super().save(commit=False)
        for name in self.fields.get("name"):
            new_tag = tag.objects.filter(name=name)
            if not new_tag.exists():
                tag.objects.create(name=name, slug=slugify(name, allow_unicode=True))
        tag.save()
        return tag
