def solution(files):
    answer = []
    tmp = []
    for file in files:
        word = ''
        head = ''
        number = ''
        for i in range(len(file)):
            if head == '':
                if '0' <= file[i] <= '9':
                    head = word
                    word = file[i]
                else:
                    word += file[i]
            else:
                if '0' <= file[i] <= '9':
                    word += file[i]
                else:
                    number = word
                    break
        if number == '':
            number = word
        head = head.upper()
        tmp.append([head, int(number), file])
    tmp = sorted(tmp, key=lambda x: x[1])
    tmp = sorted(tmp, key=lambda x: x[0])
    answer = [a[2] for a in tmp]
    return answer