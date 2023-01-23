from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib import messages
from instagram.forms import InstagramPostCreateForm
from instagram.models import Post


class InstagramPostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = InstagramPostCreateForm
    context_object_name = "post"
    template_name = "instagram/post_create.html"
    success_url = reverse_lazy("instagram:index")


    def form_valid(self, form):
        self.object = form.save(self.request)
        messages.success(self.request, "포스팅을 저장했습니다.")


        return HttpResponseRedirect(self.get_success_url())



class InstagramDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = "post"
    template_name = "instagram/post_detail.html"

    def get_object(self, queryset=None):
        queryset = self.model.objects.get(pk=self.kwargs.get("post_pk"))
        return queryset
