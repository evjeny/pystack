value = int(input("Введите пятизначное число: "))

result = (
    ((value % 100 // 10) ** (value % 10)) *
    (value % 1000 // 100) /
    (value // 10000 - value % 10000 // 1000)
)
print(result)
