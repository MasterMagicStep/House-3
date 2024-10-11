class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def Gt (self , New):
        if 0 < New <= self.floors:
            for f in range(1, New+1):
                print(f)
        else:
                print("Floor is not defined")
    def __lt__(self, other):
        return self.floors < other.floors
    def __eq__(self, other):
        return self.floors == other.floors
    def __le__ (self,other):
        return self.floors <= other.floors
    def __gt__(self,other):
        return self.floors > other.floors
    def __ge__(self, other):
        return self.floors >= other.floors
    def __ne__(self, other):
        return self.floors != other.floors
    #
    def __add__(self, value):
        self.floors += value
        return self
    def __radd__(self, other):
         return self + other
    def __iadd__(self,other):
        return self + other

    def __len__ (self):
        return self.floors
    def __str__(self):
        return (f"Название: {self.name}, количество этажей: {self.floors}")


h1 = House('Doctrine', 10)
h2 = House('Laclord', 11)
print(h1)
print(h2)
#h1.Gt(5)
#h2.Gt(12)
print(h1 < h2)
print(h1 == h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1!=h2)
print('------')
h1 += 3#add
print(h1)
h1 += 7#iadd
print(h1)
h2 = 10 +h2#radd
print(h2)
##str
#print(h1)
#print(h2)
#print('------')
##len
#print(int(len(h1)))
#print(int(len(h2)))