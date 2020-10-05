# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, start, end, target):
    if end >= start:
        pivot = (start + end) // 2
        if arr[pivot] == target:
            return pivot
        elif arr[pivot] > target:
            return binary_search(arr, start, pivot -1, target)
        else:
            return binary_search(arr, pivot + 1, end, target)
    else:
        return -1  # not found
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    b = 0
    t = len(arr) - 1
    while b < t:
        pivot = (b+t) // 2
        if target == arr[pivot]:
            return True
        elif target < pivot:
            t = pivot - 1
        else:
            b = pivot + 1
    return False
    # Your code here