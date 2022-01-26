def solution(skill, skill_trees):
    answer = 0
    tmp = dict()
    for i in range(len(skill)):
        tmp[skill[i]] = i

    for word in skill_trees:
        now = 0
        t = True
        for i in range(len(word)):
            if tmp.get(word[i], -1) > now:
                t = False
                break
            else:
                if tmp.get(word[i], -1) == now:
                    now += 1
        if t:
            answer += 1




    return answer