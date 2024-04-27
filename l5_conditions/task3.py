x = float(input("Введите X: "))
a = float(input("Введите A: "))
b = float(input("Введите B: "))

if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)
