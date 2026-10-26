def solution(num_list):
    answer1 = 0
    answer2 = 0
    for i, num in enumerate(num_list):
        if i % 2 == 0:
            answer1 += num
        else :
            answer2 += num

    if answer1 > answer2:
        return answer1
    else:
        return answer2