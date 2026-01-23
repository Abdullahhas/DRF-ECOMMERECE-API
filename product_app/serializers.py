from rest_framework import serializers
from .models import Category , Brand ,Product , User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # so password is not returned in response
        }
    
        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data['password'])
            return super().create(validated_data)






class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id' , 'name']



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

    

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"