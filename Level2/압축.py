def solution(msg):
    answer = []
    word = dict()
    last = len(msg)
    end = 27
    for i in range(ord('A'), ord('Z') + 1):
        word[chr(i)] = i - ord('A') + 1
    i=0
    while i < last:
        st = msg[i]
        now = 1
        next = ''
        while True:
            if i + now < last and word.get(msg[i:i + now + 1], -1) >= 0:
                st = msg[i: i + now + 1]
                now += 1
            else:
                if i + now < last:
                    next = msg[i: i + now + 1]
                else:
                    next = st
                break
        i += now

        if word.get(next, -1) == -1:
            word[next] = end
            end += 1
        answer.append(word[st])







    return answer