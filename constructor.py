class Phone:
    manufecturer = "Chaina"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price



    def send_message(self, phone, sms):
        text = f"Message: {sms} sent to {phone}"
        return text


my_phone = Phone("Kala chan", "Oppo", 8700)

print(my_phone.owner, my_phone.brand, my_phone.price)


her_phone = Phone("She amr jaan", "Vivo", 18000)
print(her_phone.owner, her_phone.brand, her_phone.price)