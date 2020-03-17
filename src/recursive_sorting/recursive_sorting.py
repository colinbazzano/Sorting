# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


test_array = [1, 4, 2, 5, 2, 8]
test_array2 = [9, 45, 2, 12, 5]

print(merge(test_array, test_array2))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # base case
    if len(arr) < 1:
        return arr
    # divide the array in half to recursively merge sort both
    half = len(arr) // 2
    low = merge_sort(arr[half:])
    high = merge_sort(arr[:half])
    # merge
    return merge(low, high)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
