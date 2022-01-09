def solution(n):
    n = list(str(n))
    answer = list(map(int, reversed(n)))
    return answer