from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Brand, Product, Category, Card, User , Order , OrderProduct, ProductCategory
from .serializers import BrandSerializer, OrderSerializer, UserSerializer, CategorySerializer, CardSerializer, ProductSerializer, ProductCategorySerializer, OrderProductSerializer


class UserAggregate(APIView):
    def get(self, request):
        total_users = User.objects.count()
        data = {
            'total_users': total_users
        }
        return Response(data)


class BrandList(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CardList(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetail(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCategoryList(generics.ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class OrderProductList(generics.ListCreateAPIView):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct.objects.all()


class OrderProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct.objects.all()







