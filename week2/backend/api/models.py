from django.db import models
from django.contrib.auth.models import User


class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count,
        }

class Order(models.Model):
    NO = "Add payment type"
    CARD = "Credit Card"
    CASH = "Cash"
    KASPI = "Kaspi"
    PAYMENT_TYPES = (
        (NO, "Add payment type"),
        (CARD, "Credit Card"),
        (CASH, "Cash"),
        (KASPI, "Kaspi"),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100,choices=PAYMENT_TYPES, default=NO)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    status = models.CharField(max_length=10, choices = list(zip(range(0, 1), range(0, 1))), default=0)
    
    def __str__(self):
        return '{}: {}'.format(self.id, self.product)

    def to_json(self):
        return {
            'id': self.id,
            'product': self.product,
            'payment_type': self.payment_type,
            'status': self.status,
        }
