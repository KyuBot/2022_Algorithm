def solution(n):
    answer = 0
    n = list(str(n))
    n.sort(reverse=True)
    answer = " ".join(n)
    return int(answer)