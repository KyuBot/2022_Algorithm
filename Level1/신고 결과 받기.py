def solution(id_list, report, k):
    answer = []
    min_won = dict()
    chk = [0] * len(id_list)

    for id in id_list:
        min_won[id] = set()

    for id in report:
        id_from, id_to = id.split()
        min_won[id_from] = min_won[id_from] | {id_to}
    for id in id_list:
        for name in min_won[id]:
            chk[id_list.index(name)] += 1
    for i in range(len(id_list)):
        result = 0
        f = list(min_won[id_list[i]])
        for j in range(len(f)):
            if chk[id_list.index(f[j])] >= k:
                result += 1
        answer.append(result)

    return answer

