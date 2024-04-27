n = int(input())
equal_zero = 0
for _ in range(n):
    if int(input()) == 0:
        equal_zero += 1
print(equal_zero)