from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','product_discription','product_price','user','product_category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
