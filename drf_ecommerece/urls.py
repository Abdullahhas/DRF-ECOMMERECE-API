
from django.contrib import admin
from django.urls import path
from product_app import views
from rest_framework.routers import DefaultRouter
from django.urls import path , include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView


router = DefaultRouter()
router.register(r'category' , views.CategoryView , basename='category')
router.register(r'brand' , views.BrandViewSet , basename='brand')
router.register(r'product' , views.ProductViewSet , basename='product')
# router.register(r'user' , views.UserViewSet , basename='user')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/' , SpectacularAPIView.as_view() , name = 'schema'),
    path('api/schema/docs/' , SpectacularSwaggerView.as_view(url_name = 'schema')),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')) ,
    # path('gettoken/',obtain_auth_token)
    path('gettoken/',TokenObtainPairView.as_view() , name = 'token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view() , name = 'token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view() , name = 'token_verify'),
    path('api/auth/signup',views.RegisterAPIView.as_view(), name='register'),
    path('api/auth/check/', views.CheckAuthAPIView.as_view(), name='check_auth'),
    
    
    
]
