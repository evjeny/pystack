def transform_array(array):
    return array[-1:] + array[:-1]

n = int(input())
numbers = [int(a) for a in input().split()]
print(*transform_array(numbers))