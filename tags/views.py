from django.views.generic import ListView, CreateView

from tags.forms import TagCreateForm
from tags.models import Tag
from campings.models import Camping


class TagView(ListView):
    model = Camping
    template_name = "campings/index.html"

    def get_queryset(self):
        qs = self.model.objects.filter(tag__slug=self.kwargs.get("tag_slug"))
        return qs


class TagCreateView(CreateView):
    model = Tag
    form_class = TagCreateForm
