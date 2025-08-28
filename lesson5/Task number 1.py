number = int(input("Введите число: "))
if number == 0:
    print("Нулевое число! ")
else:
    if number > 0 and number % 2 == 0:
        print("Положительное четное число! ")
    elif number < 0 and number % 2 == 0:
        print("Отрицательное четное число! ")
    else:
        print("Число не является четным! ")


    
