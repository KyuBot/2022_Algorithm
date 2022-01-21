def solution(fees, records):
    answer = []
    junsan = dict()
    money = dict()
    for rec in records:
        time, car, now = rec.split()
        if now == 'IN':
            junsan[car] = [time, 'IN']
        else:
            pre_hh, pre_mm = junsan[car][0].split(':')
            now_hh, now_mm = time.split(':')
            money[car] = money.get(car, 0) + (int(now_hh)-int(pre_hh)) * 60 + int(now_mm)-int(pre_mm)
            junsan[car][1] = 'OUT'

    for i in junsan:
        if junsan[i][1] == "IN":
            pre_hh, pre_mm = junsan[i][0].split(':')
            now_hh, now_mm = '23', '59'
            money[i] = money.get(i, 0) + (int(now_hh) - int(pre_hh)) * 60 + int(now_mm) - int(pre_mm)

    b = list(money)
    b.sort()
    print(b)
    for i in b:
        result = 0
        if money[i] - fees[0] > 0:
            if int((money[i] - fees[0]) / fees[2]) == (money[i] - fees[0]) / fees[2]:
                result = fees[1] + (money[i] - fees[0]) / fees[2] * fees[3]
            else:
                result = fees[1] + (int((money[i] - fees[0]) / fees[2]) + 1) * fees[3]
        else:
            result = fees[1]
        answer.append(result)

    return answer
