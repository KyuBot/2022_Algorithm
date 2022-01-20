def solution(price, money, count):
    answer = -1
    total = price * (count * (count+1)) / 2

    if money - total > 0:
        return 0
    else:
        return (total-money)

    return answer