def solution(n, control):
    control = control.lower()

    for i in range(len(control)):
        if control[i] == 'w' or control[i] == 'a' or control[i] == 's' or control[i] == 'd':
            if control[i] == 'w':
                n += 1
            elif control[i] == 's':
                n -= 1
            elif control[i] == 'd':
                n += 10
            elif control[i] == 'a':
                n -= 10

    return n

