def solution(numbers):
    answer = 0
    chk = [0] * 10
    for i in numbers:
        chk[i] += 1
    for i in range(len(chk)):
        if chk[i] == 0:
            answer += i
    return answer