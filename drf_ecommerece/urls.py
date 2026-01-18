
from django.contrib import admin
from django.urls import path
from product_app import views
from rest_framework.routers import DefaultRouter
from django.urls import path , include


router = DefaultRouter()
router.register(r'category' , views.CategoryView , basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
