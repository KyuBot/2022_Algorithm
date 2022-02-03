def solution(numbers):
    answer = ''
    tmp = {'0': [],
           '1': [],
           '2': [],
           '3': [],
           '4': [],
           '5': [],
           '6': [],
           '7': [],
           '8': [],
           '9': [],
           }
    for number in numbers:
        number = str(number)
        tmp[number[0]].append(number)
    for i in range(9, -1, -1):
        a = sorted(tmp[str(i)], key=lambda x:x[-1], reverse=True)
        if len(a) > 0:
            answer = answer + "".join(a)
    return answer
