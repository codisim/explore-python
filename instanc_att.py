class Shop:
    shopping_mall = "Jamuna"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # cart is an instance attribute


    def add_to_card(self, item):
        self.cart.append(item)


she = Shop("Tahar")
she.add_to_card("phone")
she.add_to_card("cake")
she.add_to_card("cha")

print(she.cart)



he = Shop("Nah")
he.add_to_card("phone")
he.add_to_card("cake")
he.add_to_card("cha")

print(he.cart)