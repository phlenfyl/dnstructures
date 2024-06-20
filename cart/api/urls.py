from django.urls import path
from .views import *



urlpatterns = [
    path('', CartDetailView.as_view(), name='cart-detail'),
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('update/<int:pk>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('delete/<int:pk>/', DeleteCartItemView.as_view(), name='delete-cart-item'),
]