person = {
    'name': 'John',
    'age': 30,
}

print(person['name']) 


person['language'] = 'English'

print(person.keys())
print(person.values())



for key, val in person.items():
    print(f'{key} : {val}')