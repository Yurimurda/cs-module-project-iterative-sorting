def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    lowest = 0
    highest = len(arr) - 1
    middle = 0

    while lowest <= highest:

        middle = (highest + lowest) // 2

        if arr[middle] < target:
            lowest = middle + 1

        elif arr[middle] > target:
            highest = middle - 1

        else:
            return middle

    return -1  # not found
