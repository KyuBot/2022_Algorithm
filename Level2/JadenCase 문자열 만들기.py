def solution(s):
    answer = ''
    tmp = 0
    for st in s:
        if st == " ":
            tmp = 0
            answer += st
        else:
            if tmp == 0:
                answer += st.upper()
                tmp = 1
            else:
                answer += st.lower()

    return answer