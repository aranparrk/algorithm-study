def solution(my_string, n):
    answer = ''

    strLen = len(my_string) - n
    answer = my_string[strLen:]
    return answer