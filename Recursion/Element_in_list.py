def Element_in_list(arr, target, start=0):
    if start == len(arr):
        return False
    return arr[start] == target or Element_in_list(arr, target, start + 1)


print(Element_in_list([2, 6, 8, 3, 5], 0))
