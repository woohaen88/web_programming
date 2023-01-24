from django import forms

from instagram.models import Post, Tag


class InstagramPostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = (
            "author",
            "tag_set",
        )
        widgets = {
            "caption": forms.Textarea(attrs={"placeholder": "태그는 '#태그명'으로 입력"}),
        }

    def save(self, request, commit=True):
        instance = super().save(commit=False)
        instance.author_id = request.user.id
        if commit:
            instance.save()
            instance.tag_set.add(*instance.extract_tag_list())
        return instance
