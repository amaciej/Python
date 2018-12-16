#!/usr/bin/env python3


def number():
    zero = 0
    num = input("Podaj dowolną liczbę ")
    num = int(num)

    if num and not zero:
        print("wpisałeś: {}".format(num))
    else:
        print("Wpisałeś liczbę równą zero")


number()


