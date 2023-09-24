def isSorted(arr, start):
    if start == len(arr) - 1:
        return True
    return arr[start] < arr[start + 1] and isSorted(arr, start + 1)


print(isSorted([1, 2, 4, 1], 0))
