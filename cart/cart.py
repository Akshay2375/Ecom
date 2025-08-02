from store.models import Product,Profile
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')  # ✅ Use 'cart' as key
        self.request=request
        if not cart:
            cart = self.session['cart'] = {}  # ✅ Initialize empty cart

        self.cart = cart
        
        
    def db_add(self,product,quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id in self.cart:
            
            pass
        else:
            self.cart[product_id] =int(product_qty)
            # self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True  # ✅ Corrected typo
        
        ## deal with logged in 
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            carty=str(self.cart)
            carty=carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))
            

    def add(self, product,quanity):
        product_id = str(product.id)
        product_qty = str(quanity)

        if product_id in self.cart:
            
            pass
        else:
            self.cart[product_id] =int(product_qty)
            # self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True  # ✅ Corrected typo
        
        ## deal with logged in 
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            carty=str(self.cart)
            carty=carty.replace("\'","\"")
            current_user.update(old_cart=str(carty))
            
        

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
       
        product_id=self.cart.keys()
        products=Product.objects.filter(id__in=product_id)
        return products
    def get_quants(self):
       
       quantities=self.cart
       return quantities
   
    def update(self, product, quantity):
        product_id = str(product)  # since product is just the ID
        product_qty = int(quantity)
    
        self.cart[product_id] = product_qty
        self.session.modified = True

        if self.request.user.is_authenticated:
                current_user=Profile.objects.filter(user__id=self.request.user.id)
                carty=str(self.cart)
                carty=carty.replace("\'","\"")
                current_user.update(old_cart=str(carty))
        thing=self.cart
            
        return thing
       
       
    def delete(self,product):
            product_id = str(product)
            
            if product_id in self.cart:
                del self.cart[product_id]
            self.session.modified = True
            if self.request.user.is_authenticated:
                current_user=Profile.objects.filter(user__id=self.request.user.id)
                carty=str(self.cart)
                carty=carty.replace("\'","\"")
                current_user.update(old_cart=str(carty))
            
            
            
    def cart_total(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        quantities=self.cart
        total=0
        for key,value in quantities.items():
            for product in products:
                key=int(key)
                if key==product.id:
                    if product.is_sale:
                         total=total+(product.sale_price*value)
                    else:
                         total=total+(product.price*value)
                    
                   
        return total