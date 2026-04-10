S = input()

result = []
new_S = ''

L = 0
R = 0

for char in S:
    new_S += char
    if char == 'L':
       L += 1
    else:
       R += 1


    if L == R:
       result.append(new_S)
       new_S = ''   
       L = 0    
       R = 0


print(len(result))
for char in result:
    print(char)