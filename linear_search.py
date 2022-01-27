'''
Linear Search Algorithm
'''

#define linear search function
def LinearSearch(list, key):
    #set found to false
    found = False

    #for each item in list
    for item in list:
        if item==key:
            found=True
            break

    return found

#create a list of numbers
numList=[12,8,31,1,77,75,18]

#key a key from the user
numKey=input("Enter a number:")

#call Linear Search function
result=LinearSearch(numList,int(numKey))

#display the result of the search
print(result)

