def solution(arr):
    if len(arr) == 1:
        return [-1]
    mm = min(arr)
    mm_index = arr.index(mm)
    arr.pop(mm_index)
    return arr