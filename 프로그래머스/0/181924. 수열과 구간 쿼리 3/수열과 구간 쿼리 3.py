def solution(arr, queries):

    for i in range(len(queries)):
        arr_num = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = arr_num


    return arr