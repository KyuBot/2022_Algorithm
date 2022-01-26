def solution(word):
    answer = 0

    tmp = ['', 'A', 'E', 'I', 'O', 'U']
    role = []

    def pick(n, st):
        nonlocal role
        nonlocal tmp

        if n == 5:
            role.append(st)
            return
        for i in range(len(tmp)):
            pick(n + 1, st + tmp[i])

    pick(0, '')

    role = set(role)
    role = list(role)
    role.sort()
    answer = role.index(word)


    return answer