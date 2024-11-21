from django.urls import path
from .views import  CategoryCreateView, \
    CategoryDetailView, CategoryListView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name="category_list_create"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
    path('category/all', CategoryListView.as_view(), name="category-list"),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name="category-update"),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name="category-delete"),
]
