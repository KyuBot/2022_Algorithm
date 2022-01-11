def solution(numbers, hand):
    answer = ''
    phone = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2], '*': [3, 0], 0: [3, 1], '#': [3, 2]
             }
    left = [3, 0]
    right = [3, 2]

    for i in numbers:
        if i in (1,4,7,'*'):
            left = phone[i]
            answer += 'L'
        elif i in (3,6,9,'#'):
            right = phone[i]
            answer += 'R'
        else:
            if abs(left[0] - phone[i][0]) + abs(left[1] - phone[i][1]) > abs(right[0] - phone[i][0]) + abs(right[1] - phone[i][1]):
                right = phone[i]
                answer += 'R'
            elif abs(left[0] - phone[i][0]) + abs(left[1] - phone[i][1]) < abs(right[0] - phone[i][0]) + abs(right[1] - phone[i][1]):
                left = phone[i]
                answer += 'L'
            else:
                if hand == 'right':
                    right = phone[i]
                    answer += 'R'
                else:
                    left = phone[i]
                    answer += 'L'


    return answer