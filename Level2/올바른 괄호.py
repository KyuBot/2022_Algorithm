def solution(s):
    answer = True
    arr = []
    for word in s:
        if word == "(":
            arr.append(word)
        else:
            if len(arr) == 0:
                return False
            else:
                if arr[-1] == "(":
                    arr.pop()
                else:
                    return False
    if len(arr) == 0:
        return True
    else:
        return False
