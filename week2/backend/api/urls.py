from django.urls import path
from api import views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.home),
    path('users/', views.UserList.as_view(), name='users'),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('categories/<int:pk>/products/', views.category_product),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/pay', views.OrderPay.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    
    path('login/', views.login),
    path('logout/', views.logout),

]
