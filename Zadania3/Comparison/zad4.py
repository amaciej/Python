#!/usr/bin/env python3


class Parallelogram:
    def __init__(self, side_length, name):
        self.side_length = side_length
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.side_length == other.side_length

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.side_length < other.side_length

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.side_length > other.side_length

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.side_length <= other.side_length

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.side_length >= other.side_length

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.side_length != other.side_length


a = Parallelogram(2, "A")
b = Parallelogram(7, "B")
h = Parallelogram(5, "H")

print("")
print("A == H = {}".format(a == h))
print("A == B = {}".format(a == b))
print("")
print("B == H = {}".format(b == h))
print("")
print("A < B = {}".format(a < b))
print("A < H = {}".format(a < h))
print("")
print("B < A = {}".format(b < a))
print("B < H = {}".format(b < h))
print("")
print("H< A = {}".format(h < a))
print("H < B = {}".format(h < b))
print("")
print("A > B = {}".format(a > b))
print("A > H = {}".format(a > h))
print("")
print("B > A = {}".format(b > a))
print("B > H = {}".format(b > h))
print("")
print("H > A = {}".format(h > a))
print("H > B = {}".format(h > b))
print("")
print("A <= B = {}".format(a <= b))
print("A <= H = {}".format(a <= h))
print("")
print("B <= A = {}".format(b <= a))
print("B <= H = {}".format(b <= h))
print("")
print("H <= A = {}".format(h <= a))
print("H <= B = {}".format(h <= b))
print("")
print("A >= B = {}".format(a >= b))
print("A >= H = {}".format(a >= h))
print("")
print("B >= A = {}".format(b >= a))
print("B >= H = {}".format(b >= h))
print("")
print("H >= A = {}".format(h >= a))
print("H >= B = {}".format(h >= b))
print("")
print("A != B = {}".format(a != b))
print("B != H = {}".format(b != h))
print("A != H = {}".format(a != h))
