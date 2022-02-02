def solution(n, words):
    answer = [0, 0]
    tmp = words[0][0]
    word = dict()
    for i in range(len(words)):
        if words[i][0] != tmp or word.get(words[i], -1) == 1:
            return [i % n + 1, i // n + 1]
        else:
            tmp = words[i][-1]
            word[words[i]] = 1


    return answer