def solution(n, wires):
    answer = 10**6

    tmp = [[0] * (n + 1) for _ in range(n+1)]
    chk = [[0] * (n + 1) for _ in range(n+1)]
    for wire in wires:
        tmp[wire[0]][wire[1]] = 1
        tmp[wire[1]][wire[0]] = 1

    def goCount(x):
        nonlocal n
        nonlocal tmp
        nonlocal arr
        for i in range(1, n+1):
            if tmp[x][i] == 1 and arr[i] == 0:
                arr[i] = 1
                goCount(i)
        return

    for i in range(1, n+1):
        for j in range(1, n+1):
            if tmp[i][j] == 1 and chk[i][j] == 0:
                tmp[i][j] = 0
                tmp[j][i] = 0
                arr = [0] * (n + 1)
                arr[i] = 1
                goCount(i)
                a = arr.count(1)
                b = n - a
                if abs(a-b) < answer:
                    answer = abs(a-b)

                tmp[i][j] = 1
                tmp[j][i] = 1
                chk[j][i] = 1

    return answer
