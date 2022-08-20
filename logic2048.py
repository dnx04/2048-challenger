import math
import random

def CheckAvailableMove(board):
    D = False
    for i in range(len(board) - 1):
        for j in range(len(board)):
            if board[i][j] != 0 and (board[i][j] == board[i + 1][j] or board[i + 1][j] == 0):
                D = True
                break
        if D:
            break
    R = False
    for i in range(len(board)):
        for j in range(len(board) - 1):
            if board[i][j] != 0 and (board[i][j] == board[i][j + 1] or board[i][j + 1] == 0):
                R = True
                break
        if R:
            break
    U = False
    for i in range(len(board) - 1, 0, -1):
        for j in range(len(board)):
            if board[i][j] != 0 and (board[i][j] == board[i - 1][j] or board[i - 1][j] == 0):
                U = True
                break
        if U:
            break
    L = False
    for i in range(len(board)):
        for j in range(len(board) - 1, 0, -1):
            if board[i][j] != 0 and (board[i][j] == board[i][j - 1] or board[i][j - 1] == 0):
                L = True
                break
        if L:
            break
    return [L,U,R,D]

def IsGameOver(board):
    chk = CheckAvailableMove(board)
    return all(mv == False for mv in chk)

def SpawnTile(board):
    if not IsGameOver(board):
        probability = random.random()
        if probability < 0.9:
            value = 2
        else:
            value = 4
        rand_list = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    rand_list.append((i, j))
        rand_pair = random.choice(rand_list)
        x, y = rand_pair[0], rand_pair[1]
        board[x][y] = value

def OperatingMove(board, direction):
    if direction == 1:
        for j in range(len(board)):
            l = -1
            for i in range(1, len(board)):
                if board[i][j] == 0:
                    continue
                for k in range(i - 1, l, -1):
                    if k == l + 1 and board[k][j] == 0:
                        board[k][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] != 0 and board[i][j] == board[k][j]:
                        board[k][j], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[k][j] != 0 and board[i][j] != board[k][j]:
                        if k != i - 1:
                            board[k + 1][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] == 0:
                        continue
    elif direction == 3:
        for i in range(len(board) - 2, -1, -1):
            l = 4
            for j in range(len(board)):
                if board[i][j] == 0:
                    continue
                for k in range(i + 1, l):
                    if k == l - 1 and board[k][j] == 0:
                        board[k][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] != 0 and board[i][j] == board[k][j]:
                        board[k][j], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[k][j] != 0 and board[i][j] != board[k][j]:
                        if k != i + 1:
                            board[k - 1][j], board[i][j] = board[i][j], 0
                        break
                    elif board[k][j] == 0:
                        continue
    elif direction == 0:
        for i in range(len(board)):
            l = -1
            for j in range(1, len(board)):
                if board[i][j] == 0:
                    continue
                for k in range(j - 1, l, -1):
                    if k == l + 1 and board[i][k] == 0:
                        board[i][k], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] != 0 and board[i][j] == board[i][k]:
                        board[i][k], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[i][k] != 0 and board[i][j] != board[i][k]:
                        if k != j - 1:
                            board[i][k + 1], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] == 0:
                        continue
    elif direction == 2:
        for i in range(len(board)):
            l = 4
            for j in range(len(board) - 2, -1, -1):
                if board[i][j] == 0:
                    continue
                for k in range(j + 1, l):
                    if k == l - 1 and board[i][k] == 0:
                        board[i][k], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] != 0 and board[i][j] == board[i][k]:
                        board[i][k], board[i][j] = board[i][j] * 2, 0
                        l = k
                        break
                    elif board[i][k] != 0 and board[i][j] != board[i][k]:
                        if k != j + 1:
                            board[i][k - 1], board[i][j] = board[i][j], 0
                        break
                    elif board[i][k] == 0:
                        continue

def GetScore(board):
    return sum(sum(i) for i in board)


"""CurBoard = [[2,2,4,8] , [4,4,4,4] , [0,2,2,4] , [4,2,2,4]]
NewBoard = OperatingMove(CurBoard,4)
print(NewBoard)"""
