x = int(input("Минимальная сумма вложений: "))
a = int(input("Сумма Майкла: "))
b = int(input("Сумма Ивана: "))

if x <= a and x <= b:
    print(2)
elif x <= a:
    print("Mike")
elif x <= b:
    print("Ivan")
elif a + b >= x:
    print("1")
else:
    print("0")
