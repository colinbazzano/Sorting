"""Merge Sort

I have finished the merge sort code and it works and passes the test, but I'd like to further implement on it to try and make it better

That is what this file is for

"""

# Create a Merge function


def merge(arrA, arrB):
    # create an empty list for result, and merge into the list
    result = []
    # create two variables i and j for tracking index position for each array
    i, j = 0, 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            result.append(arrA[i])
            i += 1
        else:
            result.append(arrB[j])
            j += 1
    result += arrA[i:]
    result += arrB[j:]
    return result

# create the merge_sort function, that takes in a list and recurses over itself


def merge_sort(arr):
    # BASE CASE!
    if len(arr) <= 1:
        # this would mean it is sorted, as it is only one element long
        return arr
    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])
    # return merge on both the high and low
    return merge(low, high)


test_list = [8, 7, 6, 5, 4]

print(merge_sort(test_list))
