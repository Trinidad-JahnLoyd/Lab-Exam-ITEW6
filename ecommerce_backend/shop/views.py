from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Product, Order, OrderItem, Cart, CartItem
from .serializers import ProductSerializer, OrderSerializer, CartSerializer, CartItemSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny] 

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if OrderItem.objects.filter(product=product).exists():
            return Response({"error": "Cannot delete product already in orders."},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))

        cart, created = Cart.objects.get_or_create(customer=user)
        product = Product.objects.get(id=product_id)

        if product.stock < quantity:
            return Response({"error": "Not enough stock"}, status=400)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        item.quantity += quantity
        item.save()
        return Response({"success": "Added to cart"})

class CheckoutViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def checkout(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(customer=user)
            items = CartItem.objects.filter(cart=cart)

            if not items.exists():
                return Response({"error": "Cart is empty"}, status=400)

            order = Order.objects.create(customer=user)
            for item in items:
                if item.product.stock < item.quantity:
                    return Response({"error": f"Not enough stock for {item.product.name}"}, status=400)
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
                item.product.stock -= item.quantity
                item.product.save()
            items.delete()
            return Response({"success": "Checkout successful"}, status=201)
        except Cart.DoesNotExist:
            return Response({"error": "Cart does not exist"}, status=400)

