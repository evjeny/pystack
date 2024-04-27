n = int(input())
numbers = [int(input()) for _ in range(n)]
reversed_numbers = numbers[::-1]
print(*reversed_numbers)
