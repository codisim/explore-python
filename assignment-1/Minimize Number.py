


def Minimize_Number():
    
    n = int(input())
    a = list(map(int, input().split()))

    operations = 0

    while True:
        all_even = True

        for i in range(n):
            if a[i] % 2 != 0:
                all_even = False
                break

        if not all_even:
            break

        for i in range(n):
            a[i] = a[i] // 2

        operations += 1

    print(operations)


Minimize_Number()


