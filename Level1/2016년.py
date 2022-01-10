def solution(a, b):
    answer = ''
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    dd = b

    for i in range(a-1):
        dd += mon[i]
    answer = day[dd % 7]


    return answer