def solution(str_list):
    answer = []
    for idx, i in enumerate(str_list):
        if i == "l":
            answer += str_list[:idx]
            break
        elif i == "r":
            answer += str_list[idx + 1:]
            break
            
    return answer