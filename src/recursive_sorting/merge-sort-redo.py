
# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # keep track of position in arrA and arrB with i and j
    # m is marking the position of the merged_arr
    i, j, m = 0, 0, 0
    while i < len(arrA) and j < len(arrB):
        print("merged_arr:", merged_arr)
        if arrA[i] <= arrB[j]:
            merged_arr[m] = arrA[i]
            i += 1
            m += 1
        elif arrA[i] > arrB[j]:
            merged_arr[m] = arrB[j]
            j += 1
            m += 1
        elif i == len(arrA):
            merged_arr[m] = arrA[i]
            m += 1
        elif j == len(arrB):
            merged_arr[m] = arrB[j]
            m += 1

    return merged_arr

    # merged_arr += arrA[i:]
    # merged_arr += arrB[j:]
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # if arr <= 1 it is sorted, so return arr
    if len(arr) <= 1:
        # Once it gets down to 1 element, it is "sorted"
        return arr
    else:
        mid = len(arr) // 2
        low = merge_sort(arr[:mid])
        high = merge_sort(arr[mid:])
    return merge(low, high)
    # merge()

    # return arr


test_list = [4, 5, 8, 3, 6, 1, 98, 34]
lst1 = [1, 2, 3]
lst2 = [3, 2, 1]

print(merge_sort(test_list))
# print(merge(lst1, lst2))
