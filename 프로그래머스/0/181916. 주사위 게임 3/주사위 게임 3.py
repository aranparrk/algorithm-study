def solution(a, b, c, d):
    answer = 0

    # 4개가 모두 같은 경우
    if a == b == c == d:
        answer = 1111 * a

    # 3개가 같은 경우
    elif a == b == c:
        p = a
        q = d
        answer = (10 * p + q) ** 2

    elif a == b == d:
        p = a
        q = c
        answer = (10 * p + q) ** 2

    elif a == c == d:
        p = a
        q = b
        answer = (10 * p + q) ** 2

    elif b == c == d:
        p = b
        q = a
        answer = (10 * p + q) ** 2

    # 2개씩 같은 경우
    elif a == b and c == d:
        p = a
        q = c
        answer = (p + q) * abs(p - q)

    elif a == c and b == d:
        p = a
        q = b
        answer = (p + q) * abs(p - q)

    elif a == d and b == c:
        p = a
        q = b
        answer = (p + q) * abs(p - q)

    # 딱 2개만 같은 경우
    elif a == b:
        answer = c * d

    elif a == c:
        answer = b * d

    elif a == d:
        answer = b * c

    elif b == c:
        answer = a * d

    elif b == d:
        answer = a * c

    elif c == d:
        answer = a * b

    # 전부 다른 경우
    else:
        answer = min(a, b, c, d)

    return answer