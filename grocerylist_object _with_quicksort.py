'''
Quicksort algorithm
'''

def partition(arr,low,high):

    i = ( low-1 )         # index of smaller element (leftmost)
    pivot = arr[high]     # take last element in array as pivot

    #for each element in the array from the given low to high index
    for j in range(low , high):
        # If leftmost element is smaller than or equal to pivot
        if  arr[j].price <= pivot.price:
            #move to next leftmost element
            i = i+1
            #swap values of low element and current element
            arr[i],arr[j] = arr[j],arr[i]

    #in
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        # pi is Partitioning Index, arr[pi] is now at right place
        pi = partition(arr,low,high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

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
#Bananas = Item("Bananas",14,2)
#Apples = Item("Apples",31,1)

#manually print object properties
#print(Bananas.qty)
#print(Bananas.price)

#print(Bananas.calculate())
#print(Apples.calculate())

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

#call the quicksort algorithm on the array
quickSort(grocerylist,0,len(grocerylist)-1)

#print each items details from the array
for x in grocerylist:
    print(x.name, x.qty, x.price)
