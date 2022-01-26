def jin(x, n):
    result = ''
    p = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while x > 0:
        result = str(p[x % n]) + result
        x //= n
    return result

def solution(n, t, m, p):
    answer = ''
    result = '0'
    chk = t * m + 1
    point = 1
    coun = 0
    while len(result) < chk:
        result += jin(point, n)
        point += 1

    for i in range(0, chk + 1, m):
        answer += result[p-1+i]
        coun += 1
        if coun == t:
            return answer