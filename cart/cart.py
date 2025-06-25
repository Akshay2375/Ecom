class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')  # ✅ Use 'cart' as key

        if not cart:
            cart = self.session['cart'] = {}  # ✅ Initialize empty cart

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            # You can extend this to add quantity later
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True  # ✅ Corrected typo

    def __len__(self):
        return len(self.cart)
