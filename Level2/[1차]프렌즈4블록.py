def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    t = True
    while t:
        t = False
        erase = []
        for i in range(m-1):
            for j in range(n-1):
                check = board[i][j]
                if check != " " and check == board[i][j+1] and check == board[i+1][j] and check == board[i+1][j+1]:
                    erase.append([i, j])
        if len(erase) > 0:
            t = True
            for er in erase:
                i, j = er[0], er[1]
                if board[i][j] != ' ':
                    board[i][j] = " "
                    answer += 1
                if board[i][j+1] != ' ':
                    board[i][j+1] = " "
                    answer += 1
                if board[i+1][j] != ' ':
                    board[i+1][j] = " "
                    answer += 1
                if board[i+1][j+1] != ' ':
                    board[i+1][j+1] = " "
                    answer += 1
        else:
            return answer
        for j in range(n):
            stack = []
            for i in range(m):
                if board[i][j] != " ":
                    stack.append(board[i][j])
            stack = [" "] * (m-len(stack)) + stack
            for i in range(m-1, -1, -1):
                board[i][j] = stack.pop()

    return answer
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])