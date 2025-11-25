# why we need oops?
#  we can build scalble large aplications
#  we can write reusable code
#  we can make code modular

#class: class is the blue print for creating objects
#object: we can buit it on blue print

class House:
    def __init__(self, floors, color, cost):  # to obj
        print(House, "self")
        self.abc = floors
        self.xyz = color
        self.mno = cost
        print(self.abc, "abc", "45")
        print(self.xyz, "zyz", "46")
        print(self.mno, "mno", "47")

House(2, "white", 20)
House(4, "orange", 100)
#why second default constructer function executing rather than 
# first on what is the reason in python 
#ans:In Python, if it seems like the second constructor function (often defined as __init__) is executing instead of the first, 
# it's likely because of method overriding—specifically, 
# only one __init__ method can exist per class
