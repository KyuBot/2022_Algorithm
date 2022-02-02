def solution(s):
    answer = 10**3 + 1
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        tmp = s[:i]
        cnt = 0
        result = ''
        t = ''
        for j in range(0, len(s), i):
            if tmp == s[j: j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    result += tmp
                else:
                    result = result + str(cnt) + tmp
                cnt = 1
                tmp = s[j: j+i]

        if cnt == 1:
            result += tmp
        else:
            result = result + str(cnt) + tmp
        if len(result) < answer:
            answer = len(result)
    return answer


