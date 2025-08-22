from django.contrib import admin
from .models import ShippingAdress,Order,OrderItem
# Register your models here.



admin.site.register(ShippingAdress)
admin.site.register(OrderItem)
admin.site.register(Order)

class OrderItemInline(admin.StackedInline):
    model=OrderItem
    extra=0

class OrderAdmin(admin.ModelAdmin):
    model=Order
    inlines=[OrderItemInline]
    readonly_fields=['date_ordered']
    fields=[ 'full_name','email','amount_paid','date_ordered','shipped','date_shipped' ]
 
    
admin.site.unregister(Order)
admin.site.register(Order,OrderAdmin)