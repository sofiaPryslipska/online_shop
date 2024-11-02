from django.urls import path
from .views import BrandList, BrandDetail, OrderList, OrderDetail, UserList, UserDetail, CategoryList, CategoryDetail, CardList, CardDetail, ProductList, ProductDetail, ProductCategoryList, ProductCategoryDetail, OrderProductList, OrderProductDetail, UserAggregate


urlpatterns = [

    path('user/aggregate/', UserAggregate.as_view(), name='user-aggregate'),
    path('brand/', BrandList.as_view()),
    path('brand/<int:pk>/', BrandDetail.as_view()),

    path('order/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),

    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),

    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),

    path('card/', CardList.as_view()),
    path('card/<int:pk>/', CardDetail.as_view()),

    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),

    path('product_category/', ProductCategoryList.as_view()),
    path('product/<int:pk>/', ProductCategoryDetail.as_view()),

    path('order_product/', OrderProductList.as_view()),
    path('order_product/<int:pk>/', OrderProductDetail.as_view()),

    ]