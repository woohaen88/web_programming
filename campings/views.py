from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from campings.forms import CampingCreateForm, CampingUpdateForm, CampingItemCreateForm
from campings.models import Camping, CampingItem, MultipleImage
from tags.forms import TagCreateForm
from tags.models import Tag


class CampingListView(ListView):
    model = Camping
    template_name = "campings/index.html"
    context_object_name = "camping_list"


class CampingDetailView(DetailView):
    model = Camping
    template_name = "campings/detail.html"
    context_object_name = "camping"

    def get_object(self, queryset=None):
        obj = self.model.objects.filter(pk=self.kwargs.get("camping_pk")).first()
        return obj


class CampingCreateView(CreateView):
    model = Camping
    context_object_name = "target_camping"
    form_class = CampingCreateForm
    success_url = reverse_lazy("campings:index")
    template_name = "campings/create.html"
    second_form_class = TagCreateForm

    def form_valid(self, form):
        # self.object = form.save(self.request)
        self.object = form.save(self.request)
        images = self.request.FILES.getlist("image")
        for image in images:
            MultipleImage.objects.create(
                images=image,
                camping_id=self.object.pk,
            )

        return HttpResponseRedirect(self.get_success_url())

    # def post(self, request, *args, **kwargs):
    #     if "form" in request.POST:
    #         form_class = self.get_form_class()
    #         form_name = "form"
    #     else:
    #         form_class = self.second_form_class
    #         form_name = "form2"
    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         return self.form_valid(form)


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


# camping Item view
class CampingItemListView(ListView):
    model = CampingItem
    template_name = "campings/camping_item_list.html"
    context_object_name = "camping_item_list"


class CampingItemCreateView(LoginRequiredMixin, CreateView):
    model = CampingItem
    template_name = "campings/camping_item_create.html"
    context_object_name = "camping_item_list"
    form_class = CampingItemCreateForm
    success_url = reverse_lazy("campings:camping_item_index")

    def form_valid(self, form):
        self.object = form.save(self.request)
        return HttpResponseRedirect(self.get_success_url())
