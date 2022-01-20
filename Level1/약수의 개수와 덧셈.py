def count_num(x):
    total = 0
    for i in range(1, x + 1):
        if x % i == 0:
            total += 1
    return total

def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        chk = count_num(i)

        if chk % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer