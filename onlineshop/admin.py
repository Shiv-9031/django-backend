from django.contrib import admin

from .models import Category,Product,Orders

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','description','id','created_at','updated_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['category','description','id','created_at','updated_at','price','image','product_name']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=['customer_name','customer_email','product','quantity','id','created_at','updated_at']

