
from django.contrib import admin
from django.urls import path
from product_app import views
from rest_framework.routers import DefaultRouter
from django.urls import path , include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView


router = DefaultRouter()
router.register(r'category' , views.CategoryView , basename='category')
router.register(r'brand' , views.BrandViewSet , basename='brand')
router.register(r'product' , views.ProductViewSet , basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/' , SpectacularAPIView.as_view() , name = 'schema'),
    path('api/schema/docs/' , SpectacularSwaggerView.as_view(url_name = 'schema'))
    
]
