def solution(arr):
    slice_arr = []

    for idx, i in enumerate(arr):
        if arr[idx] == 2:
           slice_arr.append(idx)

    if not slice_arr:
        return [-1]

    start = min(slice_arr)
    end = max(slice_arr)

    answer = arr[start:end + 1]

    return answer