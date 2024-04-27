a1 = [int(a) for a in input().split()]
visited = set()
for a in a1:
    if a in visited:
        print("YES")
    else:
        print("NO")
        visited.add(a)
