def solution(str1, str2):
    answer = 0
    st1 = dict()
    st2 = dict()
    chk = 0
    ls = 0
    ls2 = 0
    for i in range(len(str1)-1):
        s = str1[i].lower()
        s2 = str1[i+1].lower()
        if 'a' <= s <= 'z' and 'a' <= s2 <= 'z':
            st1[(s+s2)] = st1.get(s+s2, 0) + 1

    for i in range(len(str2)-1):
        s = str2[i].lower()
        s2 = str2[i+1].lower()
        if 'a' <= s <= 'z' and 'a' <= s2 <= 'z':
            st2[(s + s2)] = st2.get(s + s2, 0) + 1
    for i in st1:
        if st2.get(i, False):
            chk += min(st1[i], st2[i])
    for i in st1:
        ls += st1[i]
    for i in st2:
        ls2 += st2[i]

    if (ls + ls2 - chk) == 0 and chk == 0:
        return 65536
    return int(chk / (ls + ls2 - chk) * 65536)
