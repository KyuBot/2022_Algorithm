def solution(phone_book):
    answer = True
    phone = dict()
    for i in range(1, 21):
        phone[i] = []
    for i in phone_book:
        phone[len(i)] = phone.get(len(i)) + [i]
    for i in range(1, 20):
        if phone[i]:
            for j in range(len(phone[i])):
                c = len(phone[i][j])
                for k in range(i+1, 21):
                    for l in range(len(phone[k])):
                        if phone[i][j] == phone[k][l][:c]:
                            return False
    return answer

# def solution(phone_book):
#     answer = True
#     check = [[i, len(i)] for i in phone_book]
#     check.sort(key=lambda x: x[1])
#     for i in range(len(check)-1):
#         c = len(check[i][0])
#         for j in range(i+1, len(check)):
#             if check[i][0] == check[j][0][:c]:
#                 return False
#     return answer
