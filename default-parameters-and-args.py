

def sum(n, m):
    return n * m;


total = sum(10, 20)
print(total)    




def a_lot_of(*args):
    return (args)


def full_name(first_name, last_name):
    return f'{first_name} {last_name}'


# take paratar in serial wise
name = full_name('W', 'H')

# non serial
name2 = full_name(last_name='W', first_name='H')

print(name)




