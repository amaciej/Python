#!/usr/bin/env python3


class Cuboid:
    def __init__(self, length, name):
        self.length = length
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {} ".format(self.name, other.name))
        return self.length == other.length

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.length < other.length

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.length > other.length

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.length <= other.length

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.length >= other.length

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.length != other.length


a = Cuboid(4, "A")
b = Cuboid(5, "B")
c = Cuboid(7, "C")
d = Cuboid(9, "D")

print("A == B = {}".format(a == b))
print("A == C = {}".format(a == c))
print("A == D = {}".format(a == d))
print("")
print("B == C = {}".format(b == c))
print("B == D = {}".format(b == d))
print("")
print("C == D = {}".format(c == d))
print("")
print("A < B = {}".format(a < b))
print("A < C = {}".format(a < c))
print("A < D = {}".format(a < d))
print("")
print("B < A = {}".format(b < a))
print("B < C = {}".format(b < c))
print("B < D = {}".format(b < d))
print("")
print("C < A = {}".format(c < a))
print("C < B = {}".format(c < b))
print("C < D = {}".format(c < d))
print("")
print("D < A = {}".format(d < a))
print("D < B = {}".format(d < b))
print("D < C = {}".format(d < c))
print("")
print("A > B = {}".format(a > b))
print("A > C = {}".format(a > c))
print("A > D = {}".format(a > d))
print("")
print("B > A = {}".format(b > a))
print("B > C = {}".format(b > c))
print("B > D = {}".format(b > d))
print("")
print("C > A = {}".format(c > a))
print("C > B = {}".format(c > b))
print("C > D = {}".format(c > d))
print("")
print("D > A = {}".format(d > a))
print("D > B = {}".format(d > b))
print("D > C = {}".format(d > c))
print("")
print("A <= B = {}".format(a <= b))
print("A <= C = {}".format(a <= c))
print("A <= D = {}".format(a <= d))
print("")
print("B <= A = {}".format(b <= a))
print("B <= C = {}".format(b <= c))
print("B <= D = {}".format(b <= d))
print("")
print("C <= A = {}".format(c <= a))
print("C <= B = {}".format(c <= b))
print("C <= D = {}".format(c <= d))
print("")
print("D <= A = {}".format(d <= a))
print("D <= B = {}".format(d <= b))
print("D <= C = {}".format(d <= c))
print("")
print("A >= B = {}".format(a >= b))
print("A >= C = {}".format(a >= c))
print("A >= D = {}".format(a >= d))
print("")
print("B >= A = {}".format(b >= a))
print("B >= C = {}".format(b >= c))
print("B >= D = {}".format(b >= d))
print("")
print("C >= A = {}".format(c >= a))
print("C >= B = {}".format(c >= b))
print("C >= D = {}".format(c >= d))
print("")
print("D >= A = {}".format(d >= a))
print("D >= B = {}".format(d >= b))
print("D >= C = {}".format(d >= c))
print("")
print("A != B = {}".format(a != b))
print("A != C = {}".format(a != c))
print("A != D = {}".format(a != d))
print("")
print("B != C = {}".format(b != c))
print("B != D = {}".format(b != d))
print("")
print("C != D = {}".format(c != d))
