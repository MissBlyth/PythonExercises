#define the item object (class)
class Item:
    #initialise values of the instance
    def __init__(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price

    #print line value
    def calculate(self):
        return self.qty * self.price

#manually create instances
Bananas = Item("Bananas",14,2)
Apples = Item("Apples",31,1)

#manually print object properties
print(Bananas.qty)
print(Bananas.price)

print(Bananas.calculate())
print(Apples.calculate())


#open the groceries csv

#create an array of items from the lines in the file

#close the groceries csv


#print each item from the array


