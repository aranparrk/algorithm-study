def solution(arr):
    answer = []
    num = 0
    for i in arr:
        while num < i:
            answer.append(i)
            num += 1
        num = 0
    return answer