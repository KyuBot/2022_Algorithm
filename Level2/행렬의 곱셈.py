def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            tmp = 0
            for l in range(len(arr1[i])):
                tmp += (arr1[i][l] * arr2[l][j])
            answer[i][j] = tmp

    return answer