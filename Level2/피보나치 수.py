def solution(n):
    f1 = 1
    f2 = 0
    fibo = 0
    for i in range(n-1):
        fibo = f1+f2
        f2 = f1
        f1 = fibo
    return fibo%1234567