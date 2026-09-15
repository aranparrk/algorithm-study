def solution(a, b):
    num = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    
    return max(num, num2)