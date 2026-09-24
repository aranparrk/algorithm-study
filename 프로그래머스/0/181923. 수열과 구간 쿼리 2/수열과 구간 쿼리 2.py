def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query

        num = []

        for i in range(s, e + 1):
            if arr[i] > k:
                num.append(arr[i])

        if num:
            answer.append(min(num))
        else:
            answer.append(-1)

    return answer