from rest_framework import serializers
from shop.models import ProductImage  # Import ProductImage model
from ..models import CartItem

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', 'alt_text')  # Adjust fields as per your requirements

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_image = serializers.SerializerMethodField()
    product_alt = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = '__all__'

    def get_product_image(self, obj):
        first_image = obj.product.images.first()
        if first_image:
            return first_image.image.url
        return None

    def get_product_alt(self, obj):
        first_image = obj.product.images.first()
        if first_image:
            return first_image.alt_text
        return None