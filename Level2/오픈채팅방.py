def solution(record):
    answer = []
    tmp = dict()
    chat = []
    for records in record:
        a = records.split(" ")
        if a[0] == "Enter":
            tmp[a[1]] = a[2]
            chat.append([a[0], a[1]])
        elif a[0] == 'Change':
            tmp[a[1]] = a[2]
        else:
            chat.append([a[0], a[1]])

    for i in range(len(chat)):
        if chat[i][0] == "Enter":
            answer.append(tmp[chat[i][1]] + "님이 들어왔습니다.")
        if chat[i][0] == "Leave":
            answer.append(tmp[chat[i][1]] + "님이 나갔습니다.")


    return answer
