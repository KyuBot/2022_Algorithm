def solution(N, stages):
    answer = []
    check = [0] * (N + 2)
    stages.sort()
    pas = [len(stages)] * (N + 2)

    for i in range(len(stages)):
        check[stages[i]] += 1
    for i in range(1, len(check)):
        pas[i] = pas[i-1] - check[i-1]
    for i in range(1, len(check)-1):
        if pas[i] != 0:
            answer.append(check[i]/pas[i])
        else:
            answer.append(0)

    result = []
    for i in sorted(enumerate(answer), key=lambda x:x[1], reverse=True):
        result.append(i[0] + 1)

    return result


