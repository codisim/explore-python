
def famous_name(fisrt, last, **adition):
    name = f'{fisrt} {last}'

    # print(adition['title'])

    for key, value in adition.items():
        print(f'{key} : {value}')


    return name

name = famous_name(fisrt='Taheri', last='Ali', title='Huzur', kname='shayakh')

print(name)


def a_lot(n, m):
    sum = n + m;
    mult = n * m;
    div = n / m;
    # return [sum, mult, div];
    return sum, mult, div;

everything = a_lot(10, 20)
print(everything)