from typing import List


def Search(arr, target, index):
    New_List = []
    if index == len(arr) - 1:
        return New_List
    if arr[index] == target:
        New_List.append(index)
    Answer: List = Search(arr, target, index + 1)
    New_List.extend(Answer)
    return New_List


print(Search([1, 2, 2, 3], 2, 0))
