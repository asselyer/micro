from django.contrib import admin
from api.models import Category, Product, Order

admin.site.register(Product)
admin.site.register(Order)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by',)