from django.urls import path


from .views import (
    LotListView,
    LotDetailView,
    LotUpdateView,
    LotDeleteView,
    LotCreateView,
    CategoryListView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
)

app_name = "shop"

urlpatterns = [
    path("", LotListView.as_view(), name="lot-list"),
    path("lots/<int:pk>/", LotDetailView.as_view(), name="lot-detail"),
    path("lots/create", LotCreateView.as_view(), name="lot-create"),
    path("lots/<int:pk>/update/", LotUpdateView.as_view(), name="lot-update"),
    path("lots/<int:pk>/delete/", LotDeleteView.as_view(), name="lot-delete"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/create", CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
]
