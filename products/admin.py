from django.contrib import admin

from .models import ProductSubCategory, ProductCategory, Product


admin.site.register(ProductSubCategory)
admin.site.register(ProductCategory)
admin.site.register(Product)
