from django.shortcuts import render
from django.http import HttpResponse
from shopy.forms import *
from shopy.models import * # already imported, but just in case
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Product, CartItem # Create your views here.
from django.contrib.auth.decorators import login_required
def home(request):
    '''context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)'''
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'index.html', {'products': products})
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new product to the database
            messages.success(request, "Product added successfully.")
            return render(request,'index.html')  # Redirect to a product list or another page
        else:
            messages.error(request, "Failed to add product. Please check the form for errors.")
    else:
        form = ProductForm()  # Show an empty form for GET requests

    return render(request, 'add_product.html',{'form':form} )

def product_des(request,pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")
        return redirect('product_list')  # Redirect to the product list if not found
    
    return render(request, 'product_des.html', {'product': product})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect('home')  # or wherever your product list is
  # adjust according to your models
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{product.name} added to cart.")
        return redirect('cart')  # or redirect back to product list
    else:
        messages.error(request, "You need to be logged in to add to cart.")
        return redirect('login')
@login_required    
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})



@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        item.quantity = max(new_quantity, 1)
        item.save()
    return redirect('cart')

@login_required
def checkout(request):
    # Placeholder
    return render(request, 'checkout.html')