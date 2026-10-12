def solution(my_string, s, e):
    str1 = my_string[:s]
    str2 = my_string[s:e+1][::-1]
    str3 = my_string[e+1:]

    answer = str1 + str2 + str3

    return answer

print(solution('Progra21Sremm3', 6, 12))