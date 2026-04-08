

# with open('message.ext', 'w') as file:
#     file.write('Really, i love you, WH..!\n')


with open('message.ext', 'r') as file:
    text = file.read()
    print(text)