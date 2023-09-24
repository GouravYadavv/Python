def LinearSearch(arr, target, start=0):
    if start == len(arr):
        return -1
    elif arr[start] == target:
        return start
    return LinearSearch(arr, target, start + 1)


def List_more_than_1_index(arr, target, index, NewList_more_than_1_index=[]):
    if index == len(arr) - 1:
        return NewList_more_than_1_index
    if arr[index] == target:
        NewList_more_than_1_index.append(index)
    return List_more_than_1_index(arr, target, index + 1)


print(List_more_than_1_index([4, 2, 3, 4, 4, 4, 5], 4, 0))

print(LinearSearch([1, 2, 3, 4, 5, 6], 3))
