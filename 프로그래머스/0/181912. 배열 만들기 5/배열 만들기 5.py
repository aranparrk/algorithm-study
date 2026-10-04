def solution(intStrs, k, s, l):
    answer = []
    num = 0
    for i in intStrs:
        num = int(i[s:s+l])
        if num > k:
            answer.append(num)
    return answer