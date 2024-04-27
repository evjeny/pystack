a1 = [int(a) for a in input().split()]
a2 = [int(a) for a in input().split()]
print(len(set(a1) & set(a2)))