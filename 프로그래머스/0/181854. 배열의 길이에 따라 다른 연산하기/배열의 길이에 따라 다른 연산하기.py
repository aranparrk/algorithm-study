def solution(arr, n):
    answer = []

    for i, j in enumerate(arr):
        if len(arr) % 2 == 1 and i % 2 == 0:
            answer.append(j + n)
        elif len(arr) % 2 == 0 and i % 2 == 1:
            answer.append(j + n)
        else:
            answer.append(j)

    return answer