
n = 1
while n <= 10:
    print(n)
    n += 1

print('=============')

m = 0
while m <= 10:
    m += 1
    if m % 2 == 1:
        continue
    print(m)