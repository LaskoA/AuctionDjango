from django.views import generic
from django.urls import reverse_lazy
from shop.models import Lot, Category
from .forms import LotForm, CategoryForm, LotSearchForm


class LotListView(generic.ListView):
    model = Lot
    queryset = Lot.objects.all()
    context_object_name = "lot_list"
    template_name = "shop/lot_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LotListView, self).get_context_data(**kwargs)
        category = self.request.GET.get("category", "")
        context["search_form"] = LotSearchForm(initial={"category": category})

        return context

    def get_queryset(self):
        form = LotSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                category__title__icontains=form.cleaned_data["category"]
            )
        return self.queryset


class LotDetailView(generic.DetailView):
    model = Lot


class LotCreateView(generic.CreateView):
    model = Lot
    form_class = LotForm
    success_url = reverse_lazy("shop:lot-list")
    template_name = "shop/lot_form.html"


class LotUpdateView(generic.UpdateView):
    model = Lot
    fields = "__all__"
    success_url = reverse_lazy("shop:lot-list")
    template_name = "shop/lot_form.html"


class LotDeleteView(generic.DeleteView):
    model = Lot
    success_url = reverse_lazy("shop:lot-list")
    template_name = "shop/lot_delete.html"


class CategoryListView(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "shop/category_list.html"


class CategoryDetailView(generic.DetailView):
    model = Category


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("shop:category-list")
    template_name = "shop/category_form.html"


class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("shop:category-list")
    template_name = "shop/category_form.html"


class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy("shop:category-list")
    template_name = "shop/category_delete.html"
