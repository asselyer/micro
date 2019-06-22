from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category, Product, Order

class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        # {'name': 'new category 3'}
        # name='new category 3'
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CategorySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'name')
        # fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    payment_type = serializers.CharField(read_only=True)
  
    class Meta:
        model = Order
        fields = ('id', 'payment_type', 'product','status', 'created_by')

# class Payment(serializers.ModelSerializer):


class OrderSerializer1(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
  
    class Meta:
        model = Order
        fields = ('id', 'payment_type')

