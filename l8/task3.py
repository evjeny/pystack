m = int(input())
n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
boats = 0
while a:
    if len(a) == 1:
        boats += 1
        break
    if a[0] + a[-1] <= m:
        a.pop(0)
    a.pop()
    boats += 1
print(boats)