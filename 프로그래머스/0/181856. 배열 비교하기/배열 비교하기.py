def solution(arr1, arr2):
    num1 = 0
    num2 = 0
    
    if len(arr1) < len(arr2):
        return -1
    elif len(arr2) < len(arr1):
        return 1
    else:
        for i, j in zip(arr1, arr2):
            num1 += i
            num2 += j
            
        if num1 < num2:
            return -1
        elif num2 < num1:
            return 1
        else:
            return 0