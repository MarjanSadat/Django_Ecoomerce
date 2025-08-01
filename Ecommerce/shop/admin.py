from django.contrib import admin
from .models import *
# Register your models here.

class ProductInlineAdmin(admin.TabularInline):
    model = Product
    fields = ['name','price','picture']
    extra = 0
    
class OrderInlineAdmin(admin.TabularInline):
    model = Order
    fields = ['quality','customer']
    extra = 0

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','email']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = (ProductInlineAdmin,)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','picture']
    inlines = (OrderInlineAdmin,)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','customer','quality','address','phone','date','status']