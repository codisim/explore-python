S = input()

res = []
current = ""
balance = 0
    
for char in S:
    current += char
    if char == 'L':
        balance += 1
    else:
        balance -= 1
        
        
    if balance == 0:
        res.append(current)
        current = ""
            
    
print(len(res))
for s in res:
    print(s)

