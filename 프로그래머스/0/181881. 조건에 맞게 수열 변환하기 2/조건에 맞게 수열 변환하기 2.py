def solution(arr):
    answer = 0

    while True:
        before = arr.copy()

        for idx, i in enumerate(arr):
            if i >= 50:
                if i % 2 == 0:
                    arr[idx] = i // 2
            elif i < 50:
                if i % 2 != 0:
                    arr[idx] = i * 2 + 1

        if before == arr:
            break

        answer += 1

    return answer