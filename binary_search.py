'''
Binary Search Algorithm
'''

#create a Binary Search function
def BinarySearch(list,key):
    #set found to false
    found=False
    #get the length of the list
    iLen=len(list)
    #get the midpoint using floor division
    midP=iLen//2


    #if the key equals the midpoint
    if key == list[midP]:
        #set found to true
        found=True
    #if the length of the list is more than one item
    elif iLen > 1:
        #if the key is less than the midPoint value
        if key < list[midP]:
            #search the left side of the array
            return BinarySearch(list[:midP],key)
        else:
            #search the right side of the array
            return BinarySearch(list[midP:],key)
    #return true or false
    return found

#create an ordered list
numList=[3,6,12,27,65,98,301]

#get a key from the user
numKey=input("Enter a number:")

#call the function
result=BinarySearch(numList,int(numKey))
#print the result
print(result)
