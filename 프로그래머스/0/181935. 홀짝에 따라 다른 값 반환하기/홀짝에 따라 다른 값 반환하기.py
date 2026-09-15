def solution(n):
    num = 0

    if n % 2 == 0: # 짝수
        for i in range(1, n + 1):
            if i % 2 == 0:
                num += i ** 2
    else : # 홀수
        for i in range(1, n + 1):
            if i % 2 != 0:
                num += i

    return num
