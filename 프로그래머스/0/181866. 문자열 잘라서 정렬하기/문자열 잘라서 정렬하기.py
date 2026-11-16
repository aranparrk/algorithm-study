def solution(myString):
    answer = myString.split("x")
    result = sorted(filter(None, answer))
        
    return result