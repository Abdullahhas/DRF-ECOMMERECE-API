from django.db import models
from mptt.models import MPTTModel , TreeForeignKey
from django.contrib.auth.models import AbstractUser

#Abstract User Model
class User(AbstractUser):
    role = models.CharField(max_length=20 , choices=(('customer' , 'Customer') , ('admin' , 'Admin')) , default='customer')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username




# Category Model
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self' , on_delete=models.PROTECT , null=True , blank=True)

    def __str__(self):
        return self.name
    
    class MPTTMeta :
        order_insertion_by = ['name']





#Brand Model
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



#Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE)
    category = TreeForeignKey("Category" , on_delete=models.SET_NULL , null=True , blank=True)

    def __str__(self):
        return self.name