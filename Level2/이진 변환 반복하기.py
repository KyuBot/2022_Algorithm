def solution(s):
    answer = []
    ct = 0
    cnt = 0
    while True:
        cnt += 1
        new = ''
        for word in s:
            if word == '1':
                new += word
            else:
                ct += 1

        tmp = len(new)
        if tmp == 1:
            break
        else:
            r = ''
            while tmp > 0:
                r = str(tmp % 2) + r
                tmp //= 2
        s = r



    return [cnt, ct]