def solution(arr, idx):

    for i in range(len(arr)):
        if i >= idx:
            if arr[i] == 1:
                return i

    return -1