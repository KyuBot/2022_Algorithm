def solution(x):
    answer = True
    total = 0

    x = str(x)

    for i in range(len(x)):
        total += int(x[i])
    x = int(x)
    if x % total == 0:
        return True
    return False