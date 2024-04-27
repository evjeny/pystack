import random

def create_matrix(n, m):
    return [
        [random.randint(-10, 10) for _ in range(m)]
        for _ in range(n)
    ]


def sum_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


a = create_matrix(3, 3)
b = create_matrix(3, 3)
c = sum_matrices(a, b)
print(c)