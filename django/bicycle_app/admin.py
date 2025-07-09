from django.contrib import admin

# Register your models here.
from .models import Product, Order, Order_Item
#admin.site.register(Product)
#admin.site.register(Order)
#admin.site.register(Order_Item)

class ProductAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'product_name', 'price')

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'amount', 'order_date_time')

admin.site.register(Order, OrderAdmin)

class Order_ItemAdmin(admin.ModelAdmin):
    pass
    list_display = ('id','product_id', 'quantity', 'amount')

admin.site.register(Order_Item, Order_ItemAdmin)