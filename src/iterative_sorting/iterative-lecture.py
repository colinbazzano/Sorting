"""Selection Sort



"""


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        print(arr)
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


test_array = [5, 2, 7, 3, 8, 1]

# print(selection_sort(test_array))


def bubble_sort(arr):
    # Make a flag to show if swaps have occurred
    swaps_occurred = True
    while swaps_occurred:

        swaps_occurred = False
        # stop one early because you cannot look at the right of last el
    # For each element in the array
        for i in range(len(arr) - 1):
            print(arr)
            # Check its neighbor to the right
            # If neighbor is smaller...swap!
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    # If you get to the end and swaps have occured, start again
                swaps_occurred = True
    return arr


print(bubble_sort(test_array))


def count_sort(arr, maximum=1):

    return arr
