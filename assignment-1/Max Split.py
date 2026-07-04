



def max_split(s):
    balance_count = 0
    current_string = ""
    result = []
    
    for char in s:
        current_string += char
        if char == 'L':
            balance_count += 1
        elif char == 'R':
            balance_count -= 1
        
        if balance_count == 0:
            result.append(current_string)
            current_string = ""
            
            
    print(len(result))
    for letter in result:
        print(letter)
        
        
s = input()
max_split(s)




