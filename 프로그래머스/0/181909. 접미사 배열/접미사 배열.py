def solution(my_string):
    answer = []
    for char in range(len(my_string)):
        answer.append(my_string[char:])
        answer.sort()
    return answer