import sys
import pypyjit
from copy import deepcopy
sys.setrecursionlimit(10**7)
pypyjit.set_param('max_unroll_recursion=0')
INF = float("inf")

corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
edge = [(0, 1), (1, 0), (1, 2), (2, 1)]

a = [list(map(int, input().split())) for _ in range(3)]
resurt = []

def dfs_l(board, s1, s2):
    #print(*board, sep="\n"); print(s1, s2, '\n')

    board = deepcopy(board)
    for i in range(3):
        if (board[i][0] == 1) + (board[i][1] == 1) + (board[i][2] == 1) == 2:
            for j in range(3):
                if (board[i][j] == 0):
                    board[i][j] = 2
                    s2 += a[i][j]
                    dfs_f(board, s1, s2)
                    return
        if (board[0][i] == 1) + (board[1][i] == 1) + (board[2][i] == 1) == 2:
            for j in range(3):
                if (board[j][i] == 0):
                    board[j][i] = 2
                    s2 += a[j][i]
                    dfs_f(board, s1, s2)
                    return        
    
    if ((board[0][0] == 1) and (board[2][2] == 1)) or ((board[0][2] == 1) and (board[2][0] == 1)):
        if board[1][1] == 0:
            board[1][1] = 2
            s2 += a[1][1]
            dfs_f(board, s1, s2)
            return
        ms = -INF
        ni, nj = -1, -1
        for i, j in edge:
            if board[i][j] == 0 and ms < a[i][j]:
                ms = a[i][j]
                ni, nj = i, j
        if ms != -INF:
            board[ni][nj] = 2
            s2 += a[ni][nj]
            dfs_f(board, s1, s2)
            return
            
    if (board[0][0] == 1) + (board[1][1] == 1) + (board[2][2] == 1) == 2:
        for i in range(3):
            if (board[i][i] == 0):
                board[i][i] = 2
                s2 += a[i][i]
                dfs_f(board, s1, s2)
                return 
            
    if (board[0][2] == 1) + (board[1][1] == 1) + (board[2][0] == 1) == 2:
        for i in range(3):
            if (board[i][2-i] == 0):
                board[i][2-i] = 2
                s2 += a[i][2-i]
                dfs_f(board, s1, s2)
                return

    if board[1][1] == 0:
        board[1][1] = 2
        s2 += a[1][1]
        dfs_f(board, s1, s2)
        return
    
    cands = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                cands.append((i, j))
    
    ms = -INF
    ni, nj = -1, -1
    for i, j in cands:
        if board[i][j] == 0 and ms < a[i][j]:
            ms = a[i][j]
            ni, nj = i, j
    if ms != -INF:
        board[ni][nj] = 2
        s2 += a[ni][nj]
        dfs_f(board, s1, s2)
        return



def dfs_f(board, s1, s2):
    #print(*board, sep="\n"); print(s1, s2, '\n')

    board = deepcopy(board)
    for i in range(3):
        if (board[i][0] == 2) + (board[i][1] == 2) + (board[i][2] == 2) == 3:
            return
        if (board[0][i] == 2) + (board[1][i] == 2) + (board[2][i] == 2) == 3:
            return
    if (board[0][0] == 2) + (board[1][1] == 2) + (board[2][2] == 2) == 3:
        return
    if (board[0][2] == 2) + (board[1][1] == 2) + (board[2][0] == 2) == 3:
        return
    rem = 0
    for i in range(3):
        for j in range(3):
            rem += board[i][j] == 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1
                s1 += a[i][j]
                
                if rem <= 1:
                    c1, c2 = 0, 0
                    for x in range(3):
                        for y in range(3):
                            if board[x][y] == 1:
                                c1 += 1
                            elif board[x][y] == 2:
                                c2 += 1
                    if c1 == 5 and c2 == 4:
                        print(*board, sep="\n")
                        print(s1, s2)
                        resurt.append((s1, s2))
                else:
                    dfs_l(board, s1, s2)
                    board[i][j] = 0

dfs_f([[0] * 3 for _ in range(3)], 0, 0)
win = False
for x, y in resurt:
    if x > y:
        win = True
print("Takahashi" if win else "Aoki")