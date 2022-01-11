def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    ne = ''
    for i in new_id:
        if 'a' <= i <= 'z' or '0' <= i <= '9' or i in ('-', '_', '.'):
            ne += i
    tmp = 0
    ne3 = ''
    for i in ne:
        if i == '.':
            if tmp == 0:
                tmp = 1
        else:
            if tmp > 0:
                ne3 += '.'
                tmp = 0
            ne3 += i
    if tmp > 0:
        ne3 += '.'

    if len(ne3) != 0 and ne3[0] == '.':
        ne3 = ne3[1:]
    if len(ne3) != 0 and ne3[-1] == '.':
        ne3 = ne3[:-1]
    if ne3 == '':
        ne3 = 'a'

    if len(ne3) >= 16:
        ne3 = ne3[:15]
    if len(ne3) != 0 and ne3[-1] == '.':
        ne3 = ne3[:-1]
    if len(ne3) <= 2:
        ne3 += ne3[-1] * (3-len(ne3))

    return ne3

