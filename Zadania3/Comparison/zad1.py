#!/usr/bin/env python3

def Comparison():
    name = input("Podaj swoje imie ")
    my_name = "Adam"

    if name == my_name:
        print("Witaj {}".format(my_name))
    else:
        print("Witaj {}".format(name))

Comparison()
