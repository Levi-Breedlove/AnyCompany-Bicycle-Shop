import decimal
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages               # ← ADD THIS
from .models import Product, Order, Order_Item
from django.core.exceptions import ValidationError
import decimal


import json
import pprint                                     
from django.core import serializers

def index(request):
    print('\n***LOG: in "index" function')
    product_items = Product.objects.all()
    
    #The 4 lines below used during VIEW TESTING 
    jsondata = serializers.serialize('json', product_items)  
    json_to_runserver = json.loads(jsondata)			   	
    pprint.pprint(json_to_runserver)	                   	
    #return HttpResponse('/ page loaded. Check the runserver console for test result.')  
    context = {'product_items': product_items}    
    return render(request, "products.html", context)
    
def all_orders(request):
    print('\n***LOG: in "all_orders" function')
    orders = Order.objects.all()
    
    #The 4 lines below used during VIEW TESTING 
    jsondata = serializers.serialize('json', orders)  
    json_to_runserver = json.loads(jsondata)			   	
    pprint.pprint(json_to_runserver)	                   	
    #return HttpResponse('/order_history page loaded. Check the runserver console for test result.')  

    #The 2 lines below will be uncommented in the next lab
    context = {'orders': orders}
    return render(request, "order_history.html", context)
    
def lookup_order(request, order_id):
    order = Order.objects.get(pk=order_id)

    # Build a list of dicts so each line has a real Product object
    raw_lines = Order_Item.objects.filter(order_number=order)
    items = []
    for line in raw_lines:
        prod = Product.objects.get(pk=line.product_id)
        items.append({
            "product":  prod,
            "quantity": line.quantity,
            "amount":   line.amount,
        })

    return render(request, "order_result.html", {
        "order":         order,
        "order_details": items,
    })

def process_order(request):
    if request.method != "POST":
        return HttpResponse("process_order must receive POST")

    items = []
    total_amount = decimal.Decimal("0.00")

    # collect the lines & tally up the total
    for key, value in request.POST.items():
        if not key.startswith("quantity_"):
            continue

        qty = int(value)
        if qty == 0:
            continue

        prod_id = key.split("_", 1)[1]
        product = Product.objects.get(pk=prod_id)
        line_total = product.price * qty
        total_amount += line_total

        items.append({
            "product":  product,
            "quantity": qty,
            "amount":   line_total,
        })

    if not items:
        messages.error(request, "Please add at least one item")
        return redirect("index")

    # create the Order
    order = Order(amount=total_amount)
    order.full_clean()
    order.save()

    # persist line-items
    for line in items:
        Order_Item.objects.create(
            order_number=order,
            product_id  =line["product"].id,
            quantity    =line["quantity"],
            amount      =line["amount"],
        )

    # render exactly the same structure
    return render(request, "order_result.html", {
        "order":         order,
        "order_details": items,
    })

