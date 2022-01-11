def solution(answers):
    answer = [0, 0, 0]
    ans = []
    fi = [1, 2, 3, 4, 5]
    se = [2, 1, 2, 3, 2, 4, 2, 5]
    th = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if fi[i % len(fi)] == answers[i]:
            answer[0] += 1

        if se[i % len(se)] == answers[i]:
            answer[1] += 1

        if th[i % len(th)] == answers[i]:
            answer[2] += 1
    check = max(answer)

    for i in range(len(answer)):
        if answer[i] == check:
            ans.append(i+1)


    return ans