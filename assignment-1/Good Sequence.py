

def solve():
    line1 = input
    if not line1:
        return
    
    line2 = input()
    if not line2:
        return
    a = map(int, line2)
    
    counts = {}
    for x in a:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            
    removals = 0
    
    for x, count in counts.items():
        if count >= x:
            removals += (count - x)
        else:
            removals += count
            
    print(removals)

if __name__ == "__main__":
    solve()