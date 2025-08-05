from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


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