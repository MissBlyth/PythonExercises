'''
Selection sort

Works by cycling through a loop inside a loop, comparing the
inner loop to the outer loop and moving the element with the
smallest value into the outer loop???

'''
def SelectionSort(list):
    n = len(list)

    for i in range(0,n):
        smallest = i
        for j in range(i+1,n):
            if list[j] < list[smallest]:
                smallest = j

        if smallest !=i:
            list[smallest], list[i] = list[i],list[smallest]

    return list

#create a list to sort
example=[20, 600, 76, 512, 34, 897, 32]

#print the unordered list
print(example)

#call the function selection sort
result=SelectionSort(example)

#print the ordered list
print(result)
