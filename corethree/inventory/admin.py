from django.contrib import admin
from .models import Category, Product,Brand, Stock
# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)