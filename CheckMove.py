import math

def CheckAvailableMove(board):
    xuong = False
    for i in range(3):
        for j in range(4):
            if board[i][j] != 0 and (board[i][j] == board[i+1][j] or board[i+1][j] == 0):
                xuong = True
    phai = False
    for i in range(4):
        for j in range(3):
            if board[i][j] != 0 and (board[i][j] == board[i][j+1] or board[i][j+1] == 0):
                phai = True
    len = False
    for i in range(3,0,-1):
        for j in range(4):
            if board[i][j] != 0 and (board[i][j] == board[i-1][j] or board[i-1][j] == 0):
                len = True
    trai = False
    for i in range(4):
        for j in range(3,0,-1):
            if board[i][j] != 0 and (board[i][j] == board[i][j-1] or board[i][j-1] == 0):
                trai = True
    return [len,xuong,trai,phai]


def OperatingMove(board ,direction):
    if direction == 1:
        for j in range(4):
            l = -1
            for i in range(1,4):
                if board[i][j] == 0:
                    continue
                for k in range(i-1,l,-1):
                    if k == l + 1 and board[k][j] == 0:
                        board[k][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] !=0 and board[i][j] == board[k][j]:
                        board[k][j], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[k][j] !=0 and board[i][j] != board[k][j]:
                        if k != i - 1:
                            board[k+1][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] == 0:
                        continue
    elif direction == 2:
        for i in range(2,-1,-1):
            l = 4
            for j in range(4):
                if board[i][j] == 0:
                    continue
                for k in range(i+1,l):
                    if k == l - 1 and board[k][j] == 0:
                        board[k][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] !=0 and board[i][j] == board[k][j]:
                        board[k][j], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[k][j] !=0 and board[i][j] != board[k][j]:
                        if k != i + 1:
                            board[k-1][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] == 0:
                        continue
    elif direction == 3:
        for i in range(4):
            l = -1
            for j in range(1,4):
                if board[i][j] == 0:
                    continue
                for k in range(j-1,l,-1):
                    if k == l + 1 and board[i][k] == 0:
                        board[i][k], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] !=0 and board[i][j] == board[i][k]:
                        board[i][k], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[i][k] !=0 and board[i][j] != board[i][k]:
                        if k != j - 1:
                            board[i][k+1], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] == 0:
                        continue
    elif direction == 4:
        for i in range(4):
            l = 4
            for j in range(2,-1,-1):
                if board[i][j] == 0:
                    continue
                for k in range(j+1,l):
                    if k == l - 1 and board[i][k] == 0:
                        board[i][k], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] !=0 and board[i][j] == board[i][k]:
                        board[i][k], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[i][k] !=0 and board[i][j] != board[i][k]:
                        if k != j + 1:
                            board[i][k-1], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] == 0:
                        continue
    return board


'''CurBoard = [[2,2,4,8] , [4,4,4,4] , [0,2,2,4] , [4,2,2,4]]
NewBoard = OperatingMove(CurBoard,3)
print(NewBoard)'''