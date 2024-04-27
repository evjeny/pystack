number = int(input("Введите число: "))

if number == 0:
    print("нулевое число")
elif number > 0 and number % 2 == 0:
    print("положительное четное число")
elif number > 0 and number % 2 != 0:
    print("положительное нечетное число (число не является четным)")
elif number < 0 and number % 2 != 0:
    print("отрицательное нечетное число")
elif number < 0 and number % 2 == 0:
    print("отрицательное четное число")
