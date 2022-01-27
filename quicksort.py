'''
Quicksort Algorithm
This is a doozy.
It has two parts - the Partition algorithm chooses a pivot element,
splits the array around that element so that all lower elements are on the left side of the pivot
and all higher elements are on the right side. This results in whatever number that is the pivot
being in the correct place after the partition is performed, even though numbers on either side may still be unsorted.
The index of the correctly sorted element is then returned.

The second part, usually called the Quicksort, manages the recursive calling of the algorithm.
The whole array is sent into the quick sort, which then runs the partition function, and returns
the index of the sorted element.

Then the Quicksort function calls itself, but only the parts to the left of the already
correctly sorted element are sent in as an mini-array. The right side is then also sorted as a mini-array.

'''

def partition(arr,low,high):

    i = ( low-1 )         # index of smaller element (leftmost)
    pivot = arr[high]     # take last element in array as pivot
    print("Iteration:",i,"Pivot:", pivot)

    #for each element in the array from the given low to high index
    for j in range(low , high):
        # If leftmost element is smaller than or equal to pivot
        if  arr[j] <= pivot:
            #move to next leftmost element
            i = i+1
            #swap values of low element and current element
            print("Element less than ", pivot," swapped:", arr[i],"and", arr[j])
            arr[i],arr[j] = arr[j],arr[i]

    #in
    print("Element greater than", pivot," swapped:", arr[i+1],"and", arr[high])
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 ) 

  
# Function to do Quick sort 
def quickSort(arr,low,high):
    print("Sorting array through indexes:", low, high)
    if low < high:
        # pi is Partitioning Index, arr[pi] is now at right place
        pi = partition(arr,low,high) 
  
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  

#create an array to test the code
arr = [10, 7, 8, 9, 1, 5] 

print(arr)

n = len(arr)

quickSort(arr,0,n-1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
# This code is contributed by Mohit Kumra 
