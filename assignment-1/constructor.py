class Phone:
    manufecturer = "Apple"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price



    def send_message(self, phone, sms):
        text = f"Message: {sms} sent to {phone}"
        return text
