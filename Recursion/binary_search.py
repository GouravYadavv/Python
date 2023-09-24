from typing import List


def binary_search(arr: List, target: int, start, end: int):
    arr = sorted(arr)
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        start = mid + 1
        return binary_search(arr, target, start, end)
    else:
        end = mid - 1
        return binary_search(arr, target, start, end)


arr = [1, 2, 3, 4, 55, 66, 78]
b = binary_search(arr, 42, 0, len(arr))
print(b)
