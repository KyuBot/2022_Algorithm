def change(s):
    stack = []
    for i in range(len(s)):
        if s[i] in ('[', '{', '('):
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return 0
            if s[i] == ']':
                if '[' == stack.pop():
                    pass
                else:
                    return 0
            if s[i] == ')':
                if '(' == stack.pop():
                    pass
                else:
                    return 0
            if s[i] == '}':
                if '{' == stack.pop():
                    pass
                else:
                    return 0
    if len(stack) != 0:
        return 0
    return 1

def solution(s):
    answer = 0
    for i in range(len(s)):
        goWord = s[i:] + s[:i]
        answer += change(goWord)
    return answer


