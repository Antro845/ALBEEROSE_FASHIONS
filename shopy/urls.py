from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product',views.add_product,name="add_product"),
    path('product_des/<int:pk>',views.product_des,name="product_des"),
    path('delete/<int:pk>/', views.delete_product, name='delete-product'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),

]
