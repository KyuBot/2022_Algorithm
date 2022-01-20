def solution(lottos, win_nums):
    answer = []
    chk = [0] * 46
    cnt = 0
    nt = 0
    prise = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    for i in win_nums:
        chk[i] += 1
    for i in lottos:
        if i == 0:
            nt += 1
        if chk[i] == 1:
            cnt += 1
    return [prise[nt + cnt], prise[cnt]]