from django.contrib import admin
from .models import Product, Order, Order_Item

# ✅ Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'product_group')
    search_fields = ('product_name',)

# ✅ Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'order_date_time')

# ✅ Order Item Admin
@admin.register(Order_Item)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'quantity', 'amount')