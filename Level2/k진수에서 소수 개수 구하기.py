def prime(n):
    if n == 1:
        return 0
    a = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            a += 1
        if a > 1:
            return 0
    return 1


def solution(n, k):
    answer = 0
    jinsu = ''
    chk = ''
    while n > 0:
        jinsu = str(n % k) + jinsu
        n //= k
    for i in jinsu:
        if i != '0':
            chk += i
        else:
            if len(chk) != 0:
                answer += prime(int(chk))
            chk = ''
    if len(chk) > 0:
        answer += prime(int(chk))

    return answer
