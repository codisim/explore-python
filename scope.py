balanced = 3000

def price():
    global balanced
    print('local pricce: ', balanced)
    balanced = 500
    print('local pricce: ', balanced)
    
    
price()