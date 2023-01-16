from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from url_shortener.forms import UrlCreateForm
from url_shortener.models import ShortenedUrls
from web_programming.utils import url_count_changer


class UrlCreateView(LoginRequiredMixin, CreateView):
    template_name = "url_shortener/create.html"
    model = ShortenedUrls
    success_url = reverse_lazy("url_shortener:index")
    form_class = UrlCreateForm

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.request = self.request
    #     return form
    # def get_form(self, form_class=None):
    #     return UrlCreateForm(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        self.object = form.save(self.request)
        return HttpResponseRedirect(self.get_success_url())


class UrlUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "url_shortener/update.html"
    model = ShortenedUrls
    success_url = reverse_lazy("url_shortener:index")
    context_object_name = "target_url"
    form_class = UrlCreateForm

    def get_object(self, queryset=None):
        obj = self.model.objects.filter(pk=self.kwargs.get("url_pk")).first()
        return obj

    def form_valid(self, form):
        self.object = form.save(self.request)
        return HttpResponseRedirect(self.get_success_url())


class UrlDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "url_shortener/delete.html"
    model = ShortenedUrls
    context_object_name = "target_url"
    success_url = reverse_lazy("url_shortener:index")

    def get_object(self, queryset=None):
        obj = self.model.objects.filter(pk=self.kwargs.get("url_pk")).first()
        return obj

    def save(self, commit=True):
        instance = super().save(commit=False)
        url_data = self.model.objects.filter(user__id=self.request.user.pk)
        if commit:
            try:
                url_data.delete()
            except Exception as e:
                print(e)
            else:
                url_count_changer(self.request, False)
        return instance

    # def form_valid(self, form):
    #     self.object = form.save(self.request)
    #     return HttpResponseRedirect(self.get_success_url())


class UrlListView(LoginRequiredMixin, ListView):
    template_name = "url_shortener/index.html"
    model = ShortenedUrls
    context_object_name = "shortendurl_list"

    def get_queryset(self):
        qs = get_user_model().objects.get(pk=self.request.user.pk)
        return qs.shortened_urls.all()
