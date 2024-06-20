from django.urls import path
from .views import *



urlpatterns = [
    path('category/', CategoryList.as_view(), name= 'category'),
    path('categoryslugs/<slug:slug>/', CategorySlugsView.as_view(), name='category-slugs'),
    path('pricing/', PricingList.as_view(), name= 'pricing'),
    path('subscribe/', SubscribeList.as_view(), name= 'subscribe'),
    path('landcategory/', LandCategoryListView.as_view(), name= 'landlist'),
    path('housecategory/', HouseCategoryListView.as_view(), name= 'houselist'),
    path('product/search/', ProductSearchView.as_view(), name='product-search'),
    path('product/', ProductList.as_view(), name= 'product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/pricing/', ProductPricingView.as_view(), name='product-pricing'),
]