from django.urls import path

from .views import SubcatCreateView, SubcatDetailView, SubcatListView, SubcatUpdateView, \
    SubcatDeleteView

urlpatterns = [
    path('create/', SubcatCreateView.as_view(), name="subcategory_list_create"),
    path('subcategory/<int:pk>/', SubcatDetailView.as_view(), name="subcategory-detail"),
    path('subcategory/all', SubcatListView.as_view(), name="subcategory-list"),
    path('subcategory/update/<int:pk>/', SubcatUpdateView.as_view(), name="subcategory-update"),
    path('subcategory/delete/<int:pk>/', SubcatDeleteView.as_view(), name="subcategory-delete"),
]
