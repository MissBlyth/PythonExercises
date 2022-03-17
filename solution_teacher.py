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

class SaleRecord:
    #initialise values of the instance
    def __init__(self,suburb, salesId,dayson,reserve,price):
        self.suburb=suburb
        self.salesId=salesId
        self.dayson=dayson
        self.reserve=reserve
        self.price=price

#open the sales file csv
myFile=open("SACMOD2_2022.csv","r")

#create an array of items from the lines in the file
saleslist=[]

#read each line - for loop
for x in myFile:
    #strip new lines
    y=x.strip("\n")
    #split into array around the commas
    y=y.split(",")
    #assign array parts to instance newItem properties
    new = SaleRecord(y[0],y[1],y[2],y[3],y[4])
    #add the newitem to the groceries array
    saleslist.append(new)

#close the groceries csv
myFile.close()

#call the quicksort algorithm on the array
quickSort(saleslist,0,len(saleslist)-1)

#suburb variables
count=0
avgdays=0
total=0

#print each items details from the array
suburbs = ["Keysborough","Noble Park", "Dandenong"]
salespeople = ["AKH", "BST"]
for y in suburbs:

    for x in saleslist:
        if x.suburb == y:
            count +=1
            avgdays += int(x.dayson)
            total += int(x.price)

            for z in salespeople:
                if x.salesId == z:
                    File=open(z + ".csv","a")
                    File.write(x.suburb + "," + x.salesId + "," + x.dayson + "," + x.reserve + "," + x.price + "\n")
                    File.close()

    print(y, "total sales:", total, y,"avg days on market: ", avgdays/count)
