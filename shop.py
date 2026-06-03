class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    
    def add_to_card(self, item):
        self.cart.append(item)

she = Shop("Tahar")
she.add_to_card("phone")
she.add_to_card("cake")
she.add_to_card("cha")

print(she.cart)
