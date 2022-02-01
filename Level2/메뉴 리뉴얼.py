from itertools import combinations
def solution(orders, course):
    answer = []
    check = dict()
    for order in orders:
        for j in range(len(course)):
            if len(order) >= course[j]:
                a = list(combinations(order, course[j]))
                for i in range(len(a)):
                    s = ''
                    a[i] = list(a[i])
                    a[i].sort()
                    for k in range(len(a[i])):
                        s += a[i][k]
                    check[s] = check.get(s, 0) + 1
    for i in range(len(course)):
        r = 0
        for j in check:
            if len(j) == course[i] and check[j] > r:
                r = check[j]
        if r > 1:
            for j in check:
                if len(j) == course[i] and check[j] == r:
                    answer.append(j)
    answer.sort()



    return answer

