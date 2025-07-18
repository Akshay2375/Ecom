from store.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')  # ✅ Use 'cart' as key

        if not cart:
            cart = self.session['cart'] = {}  # ✅ Initialize empty cart

        self.cart = cart

    def add(self, product,quanity):
        product_id = str(product.id)
        product_qty = str(quanity)

        if product_id in self.cart:
            
            pass
        else:
            self.cart[product_id] =int(product_qty)
            # self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True  # ✅ Corrected typo

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

        thing=self.cart
        return thing
       
       
    def delete(self,product):
            product_id = str(product)
            
            if product_id in self.cart:
                del self.cart[product_id]
            self.session.modified = True
            
            
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