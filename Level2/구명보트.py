def solution(people, limit):
    answer = 0
    tmp = 0
    people.sort(reverse=True)
    r = 0

    while tmp < len(people):
        if r + people[tmp] <= limit:
            r += people[tmp]
        else:
            answer += 1
            r = people[tmp]
        tmp += 1


    return answer

