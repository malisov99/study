"""Задание №1

Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

top_up(X) - пополнить на X
count_1000() - выводит сколько целых тысяч осталось в кассе
take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег"""

class Kassa:
    def __init__(self, money=0):
        self.money = money

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        return self.money // 1000

    def take_away(self, x):
        if x > self.money:
            raise ValueError("Недостаточно денег в кассе")
        self.money -= x

#Пример использования
kassa = Kassa(3500)

kassa.top_up(1500)
print(kassa.money)

print(kassa.count_1000())

kassa.take_away(2000)
print(kassa.money)

kassa.take_away(4000)