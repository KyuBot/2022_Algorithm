def solution(n, m):
    answer = []
    comp = min(n, m)
    gcd = 1
    for i in range(1, comp + 1):
        if n % i == 0 and m % i == 0:
            gcm = i
    lcm = gcd * (n // gcd) * (m // gcd)

    return [gcd, lcm]

