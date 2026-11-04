def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()

    if myString.find(pat) != -1:
        answer += 1
    else:
        answer += 0

    return answer