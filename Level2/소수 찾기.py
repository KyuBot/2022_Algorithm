from itertools import permutations
def solution(numbers):
    global sosu
    answer = 0
    numbers = list(numbers)
    tmp = list(permutations(numbers, len(numbers)))
    t = set()
    for i in range(len(tmp)):
        r = "".join(tmp[i])
        t.add(r)
    print(t)
    for i in t:
        if sosu[int(i)] == 1:
            answer += 1
    return answer

sosu = [0] * 10**6
for i in range(2, 10**6):
    if sosu[i] == 0:
        sosu[i] = 1
        for j in range(2*i, 10**6, i):
            sosu[j] = 2