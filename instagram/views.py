from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin

from instagram.forms import InstagramPostCreateForm
from instagram.models import Post


class InstagramIndexView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "instagram/index.html"
    context_object_name = "post_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        suggested_user_list = (
            get_user_model()
            .objects.all()
            .exclude(pk=self.request.user.pk)
            .exclude(pk__in=self.request.user.following_set.all())[:3]
        )
        context["suggested_user_list"] = suggested_user_list
        return context


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


class UserPage(LoginRequiredMixin, DetailView):
    model = get_user_model()
    context_object_name = "user_page"
    template_name = "instagram/user_page.html"

    def get_object(self, queryset=None):
        queryset = self.model.objects.filter(
            username=self.kwargs.get("username")
        ).first()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = Post.objects.filter(author=self.get_object())
        context["post_list"] = post_list

        return context


def user_follow(request, username):
    follow_user = get_object_or_404(get_user_model(), username=username)
    request.user.following_set.add(follow_user)
    follow_user.follower_set.add(request.user)
    messages.success(request, f"{follow_user}님을 팔로우했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)


class UserFollowView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        follow_user = get_object_or_404(
            get_user_model(), username=self.kwargs.get("username")
        )
        self.request.user.following_set.add(follow_user)
        follow_user.follower_set.add(self.request.user)
        messages.success(self.request, f"{follow_user}님을 팔로우했습니다.")
        redirect_url = self.request.META.get("HTTP_REFERER", "instagram:index")
        return redirect_url


class UserUnFollowView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        unfollow_user = get_object_or_404(
            get_user_model(), username=self.kwargs.get("username")
        )
        self.request.user.following_set.remove(unfollow_user)
        unfollow_user.follower_set.remove(self.request.user)
        messages.success(self.request, f"{unfollow_user}님을 언팔로우했습니다.")
        redirect_url = self.request.META.get("HTTP_REFERER", "instagram:index")
        # return reverse("instagram:index")
        return redirect_url
