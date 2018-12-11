#!/usr/bin/env python3

class Cosmetics:
    pass

cosmetics = Cosmetics()

print(cosmetics)
print(isinstance(cosmetics, Cosmetics))
print(isinstance(cosmetics, object))

class ForFace(Cosmetics):
    pass

for_face = ForFace()

print(for_face)
print(isinstance(for_face, ForFace))
print(isinstance(for_face, Cosmetics))
print(isinstance(for_face, object))

class Fondant(ForFace):
    pass

class Powder(ForFace):
    pass

fondant = Fondant()
powder = Powder()

print(fondant)
print(isinstance(fondant,Fondant))
print(isinstance(fondant,ForFace))
print(isinstance(fondant,object))

print(powder)
print(isinstance(powder,Powder))
print(isinstance(powder,ForFace))
print(isinstance(powder,object))

print(isinstance(powder, Fondant))
print(isinstance(fondant,Powder))
