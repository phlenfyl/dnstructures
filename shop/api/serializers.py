from ..models import *
from rest_framework import serializers


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = '__all__'

class PricingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pricing
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    subscribe= SubscribeSerializer(read_only=True)
    prices= PricingSerializer(read_only=True)
    product_images = ProductImageSerializer(read_only=True, many=True, source = 'images')
    # product_image = serializers.ReadOnlyField(source = 'images.image')
    # product_alt = serializers.ReadOnlyField(source = 'images.alt')
    category_name = serializers.ReadOnlyField(source = 'category.name')
    category_slug = serializers.ReadOnlyField(source = 'category.slug')
    catsland_name = serializers.ReadOnlyField(source = 'landcategory.name')
    catsland_slug = serializers.ReadOnlyField(source = 'landcategory.slug')
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug','product']
