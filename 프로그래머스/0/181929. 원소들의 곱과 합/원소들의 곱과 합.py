def solution(num_list):
    total = 0
    product = 1

    for i in num_list:
        total += i
        product *= i

    if total ** 2 > product:
        return 1
    else:
        return 0