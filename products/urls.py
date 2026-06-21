from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart, name='cart'),

    path('increase/<path:key>/', views.increase_quantity, name='increase_quantity'),

    path('decrease/<path:key>/', views.decrease_quantity, name='decrease_quantity'),

    path('remove/<path:key>/', views.remove_item, name='remove_item'),

    path('checkout/', views.checkout, name='checkout'),

    path('success/', views.success, name='success'),

    path('launch/', views.launch, name='launch'),

    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('shoes/', views.shoes, name='shoes'),

]

path('increase/<int:id>/', views.increase_quantity, name='increase'),
path('decrease/<int:id>/', views.decrease_quantity, name='decrease'),