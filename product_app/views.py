from django.shortcuts import render
from rest_framework import viewsets
from .models import Category , Brand , Product
from .serializers import CategorySerializer , BrandSerializer , ProductSerializer
from rest_framework.response import Response


# Create your views here.

class CategoryView(viewsets.ViewSet):

    def list(self , request):
        category = Category.objects.all()
        serializer = CategorySerializer(category , many = True)
        return Response(serializer.data)
