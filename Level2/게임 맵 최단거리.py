import copy
def solution(maps):
    answer = 10**6
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = [[0, 0, 1]]
    check = [[0] * len(maps[0]) for _ in range(len(maps))]
    while len(stack):
        x, y, result = stack.pop()
        check[x][y] = result
        if x == len(maps) -1 and y == len(maps[0])-1:
            if result < answer:
                answer = result

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= len(maps) -1 and 0 <= ny <= len(maps[0]) - 1 and check[nx][ny] == 0 and maps[nx][ny] == 1:
                stack.append([nx, ny, result + 1])
            if 0 <= nx <= len(maps) -1 and 0 <= ny <= len(maps[0]) - 1 and check[nx][ny] != 0 and check[x][y] + 1 < check[nx][ny] and maps[nx][ny] == 1:
                stack.append([nx, ny, result + 1])

    if answer == 10**6:
        return -1
    return answer