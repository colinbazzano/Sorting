"""Quicksort

1. Pick you pivot
2. Create sub arrays, smaller and larger
3. Move items into sub arrays depending on pivot

[smaller] + [pivot] + [larger]

"""
import random
test_array = [23, 54, 93, 47, 55, 36, 11, 20]


def quicksort(arr):
    # Base Case: len(arr) of 1 or 0 is sorted
    if len(arr) <= 1:
        return arr
    else:
        # pick a pivot
        pivot = arr[0]
        # separate all values smaller and larger than pivot
        smaller = []
        larger = []
        for i in range(1, len(arr)):
            if arr[i] <= pivot:
                smaller.append(arr[i])
            else:
                larger.append(arr[i])
        return quicksort(smaller) + [pivot] + quicksort(larger)
        # sort smaller and larger
        # concatenate smaller + pivot + larger


print(quicksort(test_array))
