'''
Selection sort
Works by cycling through a loop inside a loop, comparing the
inner loop to the outer loop and moving the element with the
smallest value into the outer loop???
'''

#Selection sort function
def SelectionSort(list):
    #make n equal the number of elements in the list array
    n = len(list)

    #loop through each item in the array
    for i in range(0,n):
        #set current item to smallest
        smallest = i

        #cycle through the rest of the arrya
        for j in range(i+1,n):
            #if a smaller item is found, set smallest to that item
            if list[j] < list[smallest]:
                smallest = j

        #after loop, put smallest back in array
        if smallest !=i:
            list[smallest], list[i] = list[i],list[smallest]

    #sends sorted list back to the main program
    return list

#create a list to sort
example=[20, 600, 76, 512, 34, 897, 32]

example2 = ["Mailyna","Nick","Anton","Bruce","Mahi","Justin Y","Justin S","Verakarn"]



#print the unordered list
print("Unsorted list:",example)

#send example array into the function, and catch in result variable
result=SelectionSort(example)

#print the ordered list
print("Sorted list:",result)

#SORT THE SECOND LIST
#print the unordered list
print("Unsorted list:",example2)

#send example array into the function, and catch in result variable
result=SelectionSort(example2)

#print the ordered list
print("Sorted list:",result)



#sorting a data file
#open the file
myfile=open("sort_data_1.csv","r")

examplearray=[]

#read each line into an array
for x in myfile:
    y=x.strip("\n")
    y=x.split(",")
    x = (y[2] + "," + y[0] + "," + y[1] + "," + y[3] + "\n")
    examplearray.append(x)

#close the file
myfile.close()

print(examplearray)

result =SelectionSort(examplearray)

print(examplearray)
