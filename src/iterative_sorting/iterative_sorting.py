test_array = [5, 2, 7, 3, 9, 23, 1, 4]

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # (hint, can do in 3 loc)

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


print("SELECTION:", selection_sort(test_array))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # 1. loop through the array
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            # compare each element to its neighbor
            # if left el > right el, swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # 2. if no swaps performed, stop
    # else go back to the element at index - and repeat step 1

    return arr


print(bubble_sort(test_array))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
