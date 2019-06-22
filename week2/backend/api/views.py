from django.shortcuts import render
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Category, Product, Order
from api.serializers import CategorySerializer2, ProductSerializer, OrderSerializer, OrderSerializer1

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})
    

@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Category.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return CategorySerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2

def home(request):
    permission_classes = (IsAuthenticated, )
    data = User.objects.all()
    data1 = Product.objects.all()
    data2=Order.objects.all()

    return render(request, 'index.html', {'data': data, 'data1':data1, 'data2':data2})
def intro(request):
    permission_classes = (IsAuthenticated, )
    return render(request, 'intro.html')
def doc(request):
    permission_classes = (IsAuthenticated, )
    return render(request, 'doc.html')
def shop(request):
    permission_classes = (IsAuthenticated, )
    data1 = Product.objects.all()
    return render(request, 'shop.html')

def category_product(request, pk):
    permission_classes = (IsAuthenticated, )
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

class ProductList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderPay(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Order.objects.all()
    serializer_class = OrderSerializer1

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_context_data(self, **kwargs):
       
    #     context = super(UserList, self).get_context_data(**kwargs)
      
    #     context['some_data'] = 'This is just some data'
    #     return context

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

