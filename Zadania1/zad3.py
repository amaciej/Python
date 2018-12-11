#!/usr/bin/env python3
class Flower:
    def __init__(self, name, color, amount):
        self.name = name
        self.color = color
        self.amount = amount


    def opis(self):
        print("Nazwa: {}, o kolorze {} ma {} lisci".format(
            self.name, self.color, self.amount
        ))


name = input("Podaj nazwe kwiata ")
color = input("Jakiego jest koloru ")
amount = input("Ile ma lisci ")
amount = int(amount)

flower = Flower(name, color, amount)
flower.opis()
