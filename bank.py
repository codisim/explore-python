class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_wid = 100
        self.max_wid = 1000000
    
    def get_balance(self):
        return self.balance
    

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
    

    def withdraw(self, amount):
        if amount < self.min_wid:
            print(f'Fokira naki?? {self.min_wid} taha withdraw kora jai ?')
        elif amount > self.max_wid:
            print(f'Boroloker baccha naki?? {self.max_wid} taha ki bang hat pat goto kore bose thakbe???')
        else:
            self.balance -= amount
            print(f'Here is your withdraw money and remain {self.get_balance()}')
            print(f'Here is your withdraw money and remain {self.get_balance()}')


ibbl = Bank(150000000)
ibbl.withdraw(120000)