def solution(N, road, K):
    answer = 0
    tmp = [[0] * N for _ in range(N)]
    for roads in road:
        tmp[roads[0]-1][roads[1]-1] = roads[2]
        tmp[roads[1]-1][roads[0]-1] = roads[2]
    cnt = 0
    while cnt < N:



    return answer