# from itertools import permutations
# def solution(numbers):
#     global sosu
#     answer = 0
#     numbers = list(numbers)
#     tmp = list(permutations(numbers, len(numbers)))
#     t = set()
#     for i in range(len(tmp)):
#         r = "".join(tmp[i])
#         t.add(r)
#     print(t)
#     for i in t:
#         if sosu[int(i)] == 1:
#             answer += 1
#     return answer
#
# sosu = [0] * 10**6
# for i in range(2, 10**6):
#     if sosu[i] == 0:
#         sosu[i] = 1
#         for j in range(2*i, 10**6, i):
#             sosu[j] = 2

from itertools import permutations
def solution(numbers):
    answer = 0
    num = list(numbers)
    tmp = []
    for i in range(1, len(numbers)+1):
        tmp = tmp + [int("".join(i)) for i in list(permutations(num, i))]
    tmp = list(set(tmp))

    for tp in tmp:
        if tp == 0 or tp == 1:
            continue
        else:
            for i in range(2, tp):
                if tp % i == 0:
                    break
            else:
                answer += 1

    return answer