from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.category_list_create, name='category_list_create'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('products', views.product_list_create, name='product_list_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('order/create', views.create_order, name='create_order'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('cart/add', views.add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:pk>', views.delete_from_cart, name='delete_from_cart'),
]