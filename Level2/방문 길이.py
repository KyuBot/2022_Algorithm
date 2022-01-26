def solution(dirs):
    answer = 0
    now = [0, 0]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    step = dict()

    for dir in dirs:
        if dir == "U":
            next = [now[0] + dx[0], now[1] + dy[0]]

        elif dir == "D":
            next = [now[0] + dx[1], now[1] + dy[1]]
        elif dir == "L":
            next = [now[0] + dx[2], now[1] + dy[2]]
        else:
            next = [now[0] + dx[3], now[1] + dy[3]]

        if next[0] > 5 or next[1] > 5 or next[0] < -5 or next[1] < -5:
            continue

        t1 = str(now[0]) + str(next[0]) + str(now[1]) + str(next[1])
        t2 = str(next[0]) + str(now[0]) + str(next[1]) + str(now[1])


        if step.get(t1, False) or step.get(t2, False):
            pass
        else:
            step[str(t1)] = True
            step[str(t2)] = True
            answer += 1

        now[0] = next[0]
        now[1] = next[1]
    return answer
