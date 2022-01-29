def solution(line):
    answer = []
    max_x = 0
    max_y = 0
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            if line[i][0] * line[j][1] - line[i][1] * line[j][0] != 0:
                tmp = []
                x = (line[i][1]*line[j][2] - line[i][2]*line[j][1]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0])
                y = (line[i][2]*line[j][0] - line[i][0]*line[j][2]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0])
                if x == int(x) and y == int(y):
                    if abs(x) > max_x:
                        max_x = int(abs(x))
                    if abs(y) > max_y:
                        max_y = int(abs(y))

                    tmp = [x, y]
                    answer.append(tmp)
    result = [[0] * (max_x * 2 + 1) for _ in range(max_y*2 + 1)]
    print(result)


    return answer
