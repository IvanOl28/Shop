"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from shop import views

urlpatterns = [
    path('category-add/', views.category_add, name='category-add'),
    path('', views.ProductsListView.as_view(), name='category'),
    path('cart/', views.cart_view, name='cart'),
    path('detail/<int:pk>/',
         views.ProductsDetailView.as_view(), name='product-details'),
    path('add-item-to-cart/<int:pk>', views.add_item_to_cart, name='cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', views.make_order, name='make_order'),
]
