#!/usr/bin/env python3


class Car:
    def __init__(self, sedan, coupe):
        self.sedan = sedan
        self.coupe = coupe

    def __eq__(self, other):
        return self.sedan == other.sedan and self.coupe == other.coupe


car1 = Car("Tak", "Nie")
car2 = Car("Nie", "Tak")

print(car1 == car2)
print("")


class SedanCar(Car):
    def __init__(self, doors_count, length):
        self.doors_count = doors_count
        self.length = length

    def __eq__(self, other):
        return self.doors_count == other.doors_count and self.length == other.length


sedan1 = SedanCar("4", "5 metrów")
sedan2 = SedanCar("5", "6 metrów")

print(sedan1 == sedan2)
print("")


class CoupeCar(Car):
    def __init__(self, doors_count, length):
        self.doors_count = doors_count
        self.length = length

    def __eq__(self, other):
        return self.doors_count == other.doors_count and self.length == other.length


coupe1 = CoupeCar("2", "5 metrów")
coupe2 = CoupeCar("2", "5 metrów")

print(coupe1 == coupe2)
print("")


class Audi(SedanCar):
    def __init__(self, power, engine_type):
        self.power = power
        self.engine_type = engine_type

    def __eq__(self, other):
        return self.power == other.power and self.engine_type == other.engine_type


audi1 = Audi("320 KM", "Petrol")
audi2 = Audi("220 KM", "Diesel")
audi3 = Audi("320 KM", "Petrol")

print(audi1 == audi2)
print(audi2 == audi3)
print(audi1 == audi3)
print("")


class Ferrari(CoupeCar):
    def __init__(self, power, engine_type):
        self.power = power
        self.engine_type = engine_type

    def __eq__(self, other):
        return self.power == other.power and self.engine_type == other.engine_type


ferrari1 = Ferrari("460 KM", "Petrol")
ferrari2 = Ferrari("460 KM", "Petrol")
ferrari3 = Ferrari("605 KM", "Petrol")

print(ferrari1 == ferrari2)
print(ferrari2 == ferrari3)
print(ferrari1 == ferrari3)
print("")


class Maserati(CoupeCar):
    def __init__(self, power, engine_type):
        self.power = power
        self.engine_type = engine_type

    def __eq__(self, other):
        return self.power == other.power and self.engine_type == other.engine_type


maserati1 = Maserati("460 KM", "Petrol")
maserati2 = Maserati("440 KM", "Petrol")
maserati3 = Maserati("190 KM", "Petrol")

print(maserati1 == maserati2)
print(maserati2 == maserati3)
print(maserati1 == maserati2)
