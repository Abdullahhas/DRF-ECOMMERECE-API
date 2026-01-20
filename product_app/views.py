from django.shortcuts import render
from rest_framework import viewsets
from .models import Category , Brand , Product
from .serializers import CategorySerializer , BrandSerializer , ProductSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema



# Create your views here.

@extend_schema(responses = CategorySerializer)
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']
    ordering_fields = ['name']
    
    
    

@extend_schema(responses = BrandSerializer)
class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    

@extend_schema(responses=ProductSerializer)
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']
    ordering_fields = "__all__"
