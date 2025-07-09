from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("order_history", views.all_orders, name="all_orders"),
    path("lookup_order/<str:order_id>", views.lookup_order, name="lookup_order"),
    path("order_result", views.process_order, name="process_order"),
]
