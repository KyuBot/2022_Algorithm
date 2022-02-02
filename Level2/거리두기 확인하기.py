def solution(places):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = []
    for i in range(len(places)):
        answer = 1
        tmp = [[0] * 5 for _ in range(5)]
        t = True
        for j in range(len(places[i])):
            for k in range(len(places[i][j])):
                if places[i][j][k] == "P":
                    stack = [[j, k]]
                    while len(stack):
                        now = stack.pop()
                        x, y = now[0], now[1]
                        tmp[x][y] = 1
                        for m in range(4):
                            nx = x + dx[m]
                            ny = y + dy[m]
                            if 0 <= nx <= 4 and 0 <= ny <= 4 and (tmp[nx][ny] == 0):
                                if places[i][nx][ny] == "P":
                                    if abs(nx-j) + abs(ny-k) <= 2:
                                        f = True
                                        if nx == j:
                                            nny, nk = min(ny, k), max(ny, k)
                                            for l in range(nny, nk+1):
                                                if places[i][nx][l] == "X":
                                                    f = False
                                        if ny == k:
                                            nnx, nj = min(nx, j), max(nx, j)
                                            for l in range(nnx, nj+1):
                                                if places[i][l][ny] == "X":
                                                    f = False
                                        if f:
                                            answer = 0
                                            t = False
                                            break
                                elif places[i][nx][ny] == "O":
                                    stack.append([nx, ny])
                                else:
                                    continue
                        if not t:
                            break
                if not t:
                    break
            if not t:
                break
        result.append(answer)

    return result