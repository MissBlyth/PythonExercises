'''
This is a quick sort "in place" algorithm.
It is called "in place" becauae it shuffles the original elements in the array
rather than creating new arrays.

This uses "while" loops, which are more common in Python than most other languages. T
The pseudocode in your textbook uses for loops.
'''

#function partition: recives an array avariable, and information about its start and end point.
def partition(array, start, end):
    pivot = array[start]
    left = start + 1
    right = end

    # do until the loop is broken
    while True:
        # While the left marker and right marker have not crossed,
        # and the right value is on the correct side of the pivot,
        # move the right marker to the left by one place
        while left <= right and array[right] >= pivot:
            right = right - 1

        # While the left marker and right marker have not crossed,
        # and the left value is on the correct side of the pivot,
        # move the left marker to the right by one place
        while left <= right and array[left] <= pivot:
            left = left + 1

        if left <= right:
            #Swap values at left and right pointer because they are both in the wrong place
            array[left], array[right] = array[right], array[left]
            # The loop continues
        else:
            # Break the loop because the left and right markers have met
            # but theres nothing to swap
            break

    array[start], array[right] = array[right], array[start]

    return right

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print("Unsorted:", array)

quick_sort(array, 0, len(array) - 1)
print("Sorted:", array)
