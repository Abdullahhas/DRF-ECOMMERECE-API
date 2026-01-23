from django.shortcuts import render
from rest_framework import viewsets
from .models import Category , Brand , Product , User
from .serializers import CategorySerializer , BrandSerializer , ProductSerializer , UserSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from .pagination import MyPagination
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)





class CheckAuthAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": getattr(user, "role", "customer")
        })



@extend_schema(responses = CategorySerializer)
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']
    ordering_fields = ['name']
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]
    pagination_class = MyPagination
    
    
    

@extend_schema(responses = BrandSerializer)
class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]
    

@extend_schema(responses=ProductSerializer)
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']
    ordering_fields = "__all__"
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]
