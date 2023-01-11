from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView

from campings.forms import CampingCreateForm, CampingUpdateForm
from campings.models import Camping
from tags.models import Tag


class CampingListView(ListView):
    model = Camping
    template_name = "campings/index.html"
    context_object_name = "camping_list"


class CampingDetailView(DetailView):
    model = Camping
    template_name = "campings/detail.html"

    def get_object(self, queryset=None):
        obj = self.model.objects.filter(pk=self.kwargs.get("camping_pk")).first()
        return obj


class CampingCreateView(CreateView):
    model = Camping
    context_object_name = "target_camping"
    form_class = CampingCreateForm
    success_url = reverse_lazy("campings:index")
    template_name = "campings/create.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        camping = form.save(commit=False)
        camping.user = self.request.user
        camping.save()
        return valid


class CampingUpdateView(UpdateView):
    model = Camping
    template_name = "campings/update.html"
    success_url = reverse_lazy("campings:detail")
    context_object_name = "target_camping"
    form_class = CampingUpdateForm

    def get_success_url(self):
        return reverse("campings:detail", self.kwargs.get("camping_pk"))

    def get_object(self, queryset=None):
        camping_pk = self.kwargs.get("camping_pk")
        obj = self.model.objects.filter(pk=camping_pk).first()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["form"] = self.form_class(
                self.request.POST, instance=self.get_object()
            )
        return context


# def dispatch(self, request, *args, **kwargs):
#     self.object = self.get_object()
#     form_class = self.get_form_class()
#     form = self.get_form(form_class)
#     context = self.get_context_data(object=self.object, form=form)
#     return self.render_to_response(context)


# def CampingUpdateView(request, camping_pk):
#     camping = get_object_or_404(Camping, pk=camping_pk)
#
#     if request.method == "POST":
#         form = CampingUpdateForm(request.POST, instance=camping)
#         if form.is_valid():
#             camping = form.save(commit=False)
#             camping.user = request.user
#             camping.save()
#             return redirect("campings:detail", camping.pk)
#     else:
#         form = CampingUpdateForm(instance=camping)
#     context = {"form": form}
#     return render(request, "campings/update.html", context)
