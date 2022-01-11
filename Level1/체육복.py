def solution(n, lost, reserve):
    answer = 0
    answer2 = 0
    cloth = [1] * n


    for i in reserve:
        cloth[i-1] += 1

    for i in lost:
        cloth[i-1] -= 1

    cloth2 = [i for i in cloth]

    for i in range(len(cloth)-1):
        if cloth[i] == 2 and cloth[i+1] == 0:
            cloth[i] -= 1
            cloth[i+1] += 1

    for i in range(len(cloth)-1, 0, -1):
        if cloth[i] == 2 and cloth[i-1] == 0:
            cloth[i] -= 1
            cloth[i-1] += 1

    answer += cloth.count(1)
    answer += cloth.count(2)


    for i in range(len(cloth2) - 1, 0, -1):
        if cloth2[i] == 2 and cloth2[i - 1] == 0:
            cloth2[i] -= 1
            cloth2[i - 1] += 1

    for i in range(len(cloth2) - 1):
        if cloth2[i] == 2 and cloth2[i + 1] == 0:
            cloth2[i] -= 1
            cloth2[i + 1] += 1

    answer2 += cloth2.count(1)
    answer2 += cloth2.count(2)

    answer = max(answer, answer2)
    return answer