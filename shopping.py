class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []


    def add_to_cart(self, item, price, quantity):

        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)

        # self.item  = item
        # self.price = price
        # self.quantity = quantity


    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item, total)
            total += item['price'] * item['quantity']
        print("total price: ", total)



swapon = Shopping("Alan Swapon")
swapon.add_to_cart("pan", 5, 5)
swapon.add_to_cart("pani", 9, 12)
swapon.add_to_cart("cha", 8, 10)

# print(swapon.cart)
swapon.checkout(500)


    