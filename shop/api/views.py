from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from ..models import *
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100


# class ProductSearchView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class = StandardResultsSetPagination
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     search_fields = ['name', 'info', 'category__name', 'landcategory__name']

class ProductSearchView(generics.ListAPIView):
    def get_queryset(self):
        result = super(Search, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            object_list = Product.objects.filter(landcategory__name__icontains = query).distinct()
            serializer = ProductSerializer(object_list, many = True)
            return Response(serializer.data)
        else:
            return Response([])

# class ProductSearchView(APIView):
#     def get(self, request):
#         search_query = request.query_params.get('search', None)
#         if search_query:
#             products = Product.objects.filter(
#                 Q(name__lower__icontains=search_query.lower()) |
#                 Q(landcategory__name__lower__icontains=search_query.lower()) |
#                 Q(category__name__lower__icontains=search_query.lower())
#             ).distinct()

#             serializer = ProductSerializer(products, many=True)
#             return Response(serializer.data)
#         return Response([])

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend ]
    search_fields =['name']

class PricingList(generics.ListAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class SubscribeList(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class CategorySlugsView(APIView):
    pagination_class = StandardResultsSetPagination
    def get(self, request, slug, *args, **kwargs):
        # Retrieve all products
        products = Product.objects.filter(category__slug=slug) | Product.objects.filter(landcategory__slug=slug)

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)
        
        # Serialize the products
        serializer = ProductSerializer(paginated_products, many=True)
        
        return paginator.get_paginated_response(serializer.data)

class LandCategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        # slug = self.kwargs['slug']
        return Category.objects.exclude(categorychoice='house')

class HouseCategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.exclude(categorychoice='land')

class ProductList(APIView):
    pagination_class = StandardResultsSetPagination
    def get(self, request, *args, **kwargs):
        # Retrieve all products
        products = Product.objects.all()

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)
        
        # Serialize the products
        serializer = ProductSerializer(paginated_products, many=True)
        
        return paginator.get_paginated_response(serializer.data)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPricingView(APIView):
    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, id=pk)
        pricing = product.prices
        serializer = PricingSerializer(pricing)
        return Response(serializer.data)


# class CategoryList(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'

#     filter_backends = [filters.SearchFilter, DjangoFilterBackend ]
#     search_fields =['name']
# class HouseCategoryRetrieve(generics.RetrieveAPIView):
#     lookup_field = 'slug'
#     serializer_class = CategorySerializer
#     queryset = Category.objects.exclude(housecats__isnull=True)



# class LandCategoryRetrieve(generics.RetrieveAPIView):
#     lookup_field = 'slug'
#     serializer_class = CategorySerializer
#     queryset = Category.objects.exclude(landcats__isnull=True)