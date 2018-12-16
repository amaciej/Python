#!/usr/bin/env python3


def comparison():
    name = input("Podaj swoje imie ")
    my_name = "Adam"

    if name == my_name:
        print("Witaj {}, mamy takie samo imię".format(my_name))
    else:
        print("Witaj {}".format(name))


comparison()
