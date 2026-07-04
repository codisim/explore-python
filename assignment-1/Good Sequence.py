


def Good_Sequence():
    n = int(input())
    a = list(map(int, input().split()))

    freq = {}

    for i in range(n):
        num = a[i]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    removals = 0

    for x, count in freq.items():
        if count < x:
            removals += count
        else:
            removals += count - x

    print(removals)


Good_Sequence()



