def solution(myString):
    answer = myString.split("x")
    idx = []
    for i in answer:
        idx.append(len(i))
    return idx