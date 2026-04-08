def mult():
    return 3, 4

things = 'pen', 'book', 'paper', 'whiteboard', 'marker'


print(len(things))
# print(things[3])
# print(things[-2])


if 'pen' in things:
    print('Yes, pen is in the things tuple')


for thi in things:
    print(thi)


mega = ([1, 2, 3, 4], [9, 23, 42, 56], [0, 1, 2, 3])

mega[1][1] = 00

print(mega)