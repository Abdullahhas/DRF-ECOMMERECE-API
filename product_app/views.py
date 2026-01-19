from django.shortcuts import render
from rest_framework import viewsets
from .models import Category , Brand , Product
from .serializers import CategorySerializer , BrandSerializer , ProductSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


# Create your views here.

class CategoryView(viewsets.ViewSet):

    @extend_schema(responses = CategorySerializer)
    def list(self , request):
        category = Category.objects.all()
        serializer = CategorySerializer(category , many = True)
        return Response(serializer.data)
    


class BrandViewSet(viewsets.ViewSet):

    @extend_schema(responses = BrandSerializer)
    def list(self , request):
        category = Brand.objects.all()
        serializer = BrandSerializer(category , many = True)
        return Response(serializer.data)
    

class ProductViewSet(viewsets.ViewSet):

    @extend_schema(responses=ProductSerializer)
    def list(self , request):
        product = Product.objects.all()
        serializer = ProductSerializer(product , many = True)
        return Response(serializer.data)
