def solution(sizes):
    chk1 = 0
    chk2 = 0

    for i in range(len(sizes)):
        a = sizes[i][0]
        b = sizes[i][1]
        a, b = max(a, b), min(a, b)
        if a > chk1:
            chk1 = a
        if b > chk2:
            chk2 = b

    return chk1 * chk2
