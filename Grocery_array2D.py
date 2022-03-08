'''
Sorting the grocery List
'''
#open the grocery list file
myFile=open("grocerylist.csv","r")

#create a blank array
myGroceries =[]

#cycle through each line in the file as x
for x in myFile:
    y = x.strip("\n") #remove line endings
    y=y.split(",") #convert to an array around commas
    myGroceries.append(y) #add item to0 the array

#close the grocery list file
myFile.close()
#print the whole dang array
print(myGroceries)
#print the first item in the array
print(myGroceries[0])
#print the first item in the item array
print(myGroceries[0][0])


#calculate the total cost of the list

total = 0

for x in myGroceries:
   total += int(x[1]) * int(x[2].strip("$"))

print(total)
