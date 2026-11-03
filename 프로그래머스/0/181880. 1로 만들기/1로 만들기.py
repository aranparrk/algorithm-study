def solution(num_list):
    answer = 0
    num = 0
    for i in num_list:
        answer = i
        while True:
            
            if answer == 1:
                break;
            elif answer % 2 == 0:
                answer = answer // 2
                num += 1 
            else:
                answer = (answer - 1) // 2
                num += 1
            
                
    return num