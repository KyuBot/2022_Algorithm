def solution(x, n):
    answer = [x] * n
    for i in range(len(answer)):
        answer[i] = x * (1 + i)
    return answer