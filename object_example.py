
#defining a class
class Dog:
    def __init__(self, name, age, cutelvl):
        self.name = name
        self.age = age
        self.cutelvl = cutelvl

    def Woof(self):
        print(self.name, "Woof woof woof")

Dogs =[]

#create objects

Bruno = Dog("Bruno",12,52377)
Tia = Dog("Tia", 12, 68394)

Dogs.append(Bruno)
Dogs.append(Tia)

Dogs[0].Woof()
Dogs[1].Woof()
