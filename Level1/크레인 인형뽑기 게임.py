def solution(board, moves):
    answer = 0
    toy = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(toy) == 0:
                    toy.append(board[j][i-1])
                else:
                    if toy[-1] == board[j][i-1]:
                        toy.pop()
                        answer += 2
                    else:
                        toy.append(board[j][i-1])
                board[j][i-1] = 0
                break

    return answer