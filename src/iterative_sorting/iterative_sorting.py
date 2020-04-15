# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    # Loop through the array
    for i in range(0, len(arr)):
        print("array at start", arr)
        for j in range(i+1, len(arr)):
            # Compare each element to its neighbor
            if arr[i] > arr[j]:
                # if elements are in wrong position, swap them
                # print("I and J before:", arr[i], arr[j])
                arr[i], arr[j] = arr[j], arr[i]
                # print("I and J after:", arr[i], arr[j])

    # If no swaps were performed, stop, else go back to the element at index 0 and repeat step 1
    return arr


test_list = [4, 3, 64, 24, 2]

print(bubble_sort(test_list))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
