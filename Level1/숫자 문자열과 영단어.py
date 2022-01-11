def solution(s):
    s = list(s)
    answer = ''
    now = ''
    num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    for i in s:
        if '0' <= i <= '9':
            answer += i
        else:
            now += i
            if 0 <= num.get(now, 11) <= 9:
                answer += str(num.get(now))
                now = ''

    return int(answer)