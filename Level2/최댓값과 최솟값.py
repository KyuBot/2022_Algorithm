def solution(s):
    answer = ''
    mynum = []
    check = 0
    tmp = ""
    for st in s:
        if st == " ":
            mynum.append(int(tmp))
            tmp = ''
            check = 0
        else:
            tmp += st
    mynum.append(int(tmp))


    return "{} {}".format(min(mynum), max(mynum))