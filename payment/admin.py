from django.contrib import admin
from .models import ShippingAdress,Order,OrderItem
# Register your models here.


admin.site.register(ShippingAdress)
admin.site.register(OrderItem)
admin.site.register(Order)