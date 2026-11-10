def solution(myString, pat):
    answer = myString.rfind(pat)
    
    myString = myString[:answer + len(pat)]
    
    return myString