from django.contrib import admin
from shopy.models import *
from .models import Category, Product
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
