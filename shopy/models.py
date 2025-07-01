from django.db import models
from django.contrib.auth.models import User
from django.core.files.images import ImageFile

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)
    phone_field=models.CharField(max_length=12,blank=False)
    def __str__(self):
        return self.user.username
class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.FloatField(default=0.0)
    product_available_count = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

