def solution(n):
    answer = 0
    def change(x):
        line = ''
        while x > 0:
            line = str(x%2) + line
            x //= 2
        return line
    chk = change(n).count('1')

    def change2(x):
        line = ''
        nonlocal chk
        while x > 0:
            line = str(x%2) + line
            x //= 2

            if line.count('1') > chk:
                return '0'
        return line

    for i in range(n+1, 10**6):
        if chk == change2(i).count('1'):
            return i


    return answer