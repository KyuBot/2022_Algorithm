def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(numbers[i] + 1, 10**15+1):
            r = numbers[i] ^ j

            re = ''
            cnt = 0
            t = True
            while r > 0:
                if r % 2 == 1:
                    cnt += 1
                if cnt > 2:
                    t = False
                    break
                r //= 2
            if t:
                answer.append(j)
                break

    return answer
