from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from shop.models import Product, Pricing
from ..models import CartItem
from .serializers import CartItemSerializer

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        print(user.id)
        product_id = request.data.get('product_id')
        item_price = int(float(request.data.get('itemprice')))
        plan_name = request.data.get('plan_name')
        quantity = request.data.get('quantity', 1)

        product = get_object_or_404(Product, id=product_id)        
        try:     
            cart_item, item_created = CartItem.objects.get_or_create(
                user_id=user.id,
                product_id=product.id,
                item_price=item_price,
                item_paid = False,
                plan_name = plan_name,
                quantity= quantity
            )

            if not item_created:
                cart_item.quantity += quantity
                cart_item.save()

            print('success')
            return Response({'message': 'Item added to cart successfully'})
        except:
            print('nope')
            return Response({'error': 'Item not added'})



class UpdateCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        user = request.user.email
        cart_item = get_object_or_404(CartItem, id=pk, user__email=user)
        quantity = request.data.get('quantity', 1)

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            return Response({'message': 'Cart item updated successfully'})
        else:
            cart_item.delete()
            return Response({'message': 'Cart item removed successfully'})
        


class DeleteCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        user = request.user
        cart_item = get_object_or_404(CartItem, id=pk, user_id=user.id)
        cart_item.delete()
        return Response({'message': 'Cart item deleted successfully'})
    

class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        cart = get_list_or_404(CartItem, user_id=user.id)
        print(cart)
        serializer = CartItemSerializer(cart, many= True)
        return Response(serializer.data)
