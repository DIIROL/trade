# products/urls.py

from django.urls import path
from . import view

urlpatterns = [
    path('', view.product_list, name='product_list'),
    path('product/<int:pk>/', view.product_detail, name='product_detail'),
    path('product/new/', view.product_create, name='product_create'),
    path('product/<int:pk>/edit/', view.product_update, name='product_update'),
    path('product/<int:pk>/delete/', view.product_delete, name='product_delete'),
]
