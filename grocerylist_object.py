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
myFile=open("grocerylist.csv","r")
#create an array of items from the lines in the file
grocerylist=[]

    #read each line - for loop
for x in myFile:
    #strip new lines
    y=x.strip("\n")
    #split into array around the commas
    y=y.split(",")
    #assign array parts to instance newItem properties
    new = Item(y[0],y[1],y[2])
    #add the newitem to the groceries array
    grocerylist.append(new)

#close the groceries csv
myFile.close()

#print each items details from the array
for x in grocerylist:
    print(x.name, x.qty, x.price)
