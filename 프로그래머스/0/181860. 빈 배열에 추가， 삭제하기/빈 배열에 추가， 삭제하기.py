def solution(arr, flag):
    answer = []
    num = 0
    for i, j in zip(arr, flag):
        if j:
            num = i * 2
            for z in range(num):
                answer.append(i)
        else:
            del answer[-i:]
            
    
        
    return answer