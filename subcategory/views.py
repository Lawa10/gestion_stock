from django.shortcuts import render
from django.views.generic import DetailView
from requests import Response
from rest_framework import generics
from unicodedata import category

from .models import SubCategory
from .serializers import SubSerializers



# Create your views here.

class SubcatCreateView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubSerializers

class SubcatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubSerializers

class SubcatListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubSerializers

class SubcatUpdateView(generics.RetrieveUpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubSerializers
    partial = True

class  SubcatDeleteView(generics.DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Category"))
