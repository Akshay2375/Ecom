from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)


## Mix profile inof and user info:
class ProfileInline(admin.StackedInline):
    model=Profile
    # extend user model
class UserAdmin(admin.ModelAdmin):
    model=User
    fields=["username","first_name","last_name","email"]
    inlines=[ProfileInline]
    
admin.site.unregister(User)
admin.site.register(User,UserAdmin)