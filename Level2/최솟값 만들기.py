def solution(A,B):
    answer = []

    A.sort()
    B.sort(reverse=True)
    answer = [ A[i] * B [i] for i in range(len(A))]
    return sum(answer)