from django.db import models
from django.contrib.auth.models import  User
from store.models import Product
# Create your models here.
from django.db.models.signals import post_save,pre_save
import datetime
from django.dispatch import receiver

class ShippingAdress(models.Model):
    
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shipping_address2=models.CharField(max_length=200, blank=True,null=True)
    shipping_full_name=models.CharField(max_length=200, blank=True,null=True)
    shipping_email=models.CharField(max_length=200, blank=True,null=True)
    shipping_address1=models.CharField(max_length=200, blank=True,null=True)
    shipping_city=models.CharField(max_length=200, blank=True,null=True)
    
    
    class Meta:
        verbose_name_plural='Shipping Address'
        
    def __str__(self):
        return f'Shipping Adress-{str(self.id)}'
    
    
def create_shipping(sender,instance,created,**kwargs):
    if created:
        user_shipping=ShippingAdress(user=instance)
        user_shipping.save()
        
post_save.connect(create_shipping,sender=User)
    
    
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200 )  
    email=models.EmailField( max_length=200)  
    shipping_address=models.TextField(max_length=2500)
    amount_paid=models.DecimalField(max_digits=8,decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)
    shipped=models.BooleanField(default=False)
    date_shipped=models.DateTimeField(blank=True,null=True)
       
    def __str__(self):
        return f' order-{str(self.id)}'
    
    
@receiver(pre_save, sender=Order)
def set_shipped_date(sender,instance, **kwargs):
    if instance.pk:   
     now=datetime.datetime.now()
     obj=sender._default_manager.get(pk=instance.pk)
     if instance.shipped and not obj.shipped:
         instance.date_shipped=now


class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE )
    quantity=models.BigIntegerField(default=1)
    price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f' order Item -{str(self.id)}'