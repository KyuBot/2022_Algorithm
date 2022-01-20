import math

def lcm(x, y):
    gcd = math.gcd(x, y)

    return gcd * (x // gcd) * (y // gcd)

def solution(arr):
    answer = 0
    tmp = arr[0]

    for comp in arr:
        answer = lcm(tmp, comp)
        tmp = answer

    return answer