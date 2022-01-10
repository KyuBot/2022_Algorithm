def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                pass
            else:
                return False
    else:
        return False
    return answer