from  collections import deque,defaultdict
from copy import deepcopy

VERTICAL = 'v'
HORIZONTAL = 'h'
DIAGONAL = 'd'
ANTIDIAGONAL = 'a'

def equals(m1,m2):
    m1 = m1[:]
    m2 = m2[:]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if m1[i][j] != m2[i][j]:
                return False
    return True

def transpose(matrix,selected_range,direction):
    matrix_t = deepcopy(matrix)

    left_up,right_down = selected_range
    luy,lux = left_up[0],left_up[1]
    rdy,rdx = right_down[0],right_down[1]
    P = rdy - luy + 1
    Q = rdx - lux + 1
    if P <= 1 and Q <= 1:
        return matrix_t

    if direction == VERTICAL: # 縦軸
        for i in range(lux,rdx+1):
            matrix_t[luy][i],matrix_t[rdy][i] = matrix_t[rdy][i],matrix_t[luy][i]

    if direction == HORIZONTAL: # 横軸
        for i in range(luy,rdy+1):
            matrix_t[i][lux],matrix_t[i][rdx] = matrix_t[i][rdx],matrix_t[i][lux]

    if direction == DIAGONAL: # 左から右の対角線
        if P == Q == 2:
            matrix_t[luy][lux],matrix_t[rdy][rdx] = matrix_t[rdy][rdx],matrix_t[luy][lux]
        elif P == Q == 3:
            matrix_t[0][1],matrix_t[1][0] = matrix_t[1][0],matrix_t[0][1]
            matrix_t[0][2],matrix_t[2][0] = matrix_t[2][0],matrix_t[0][2]
            matrix_t[1][2],matrix_t[2][1] = matrix_t[2][1],matrix_t[1][2]
    
    if direction == ANTIDIAGONAL: # 右から左の対角線
        if P == Q == 2:
            matrix_t[luy][rdx],matrix_t[rdy][lux] = matrix_t[rdy][lux],matrix_t[luy][rdx]
        elif P == Q == 3:
            matrix_t[0][0],matrix_t[2][2] = matrix_t[2][2],matrix_t[0][0]
            matrix_t[0][1],matrix_t[1][2] = matrix_t[1][2],matrix_t[0][1]
            matrix_t[1][0],matrix_t[2][1] = matrix_t[2][1],matrix_t[1][0]        
    return matrix_t


def mat_to_str(matrix):
    return ''.join([''.join(row) for row in matrix])

def solve(H,W,S,T):

    if equals(S,T):
        print(0)
        exit()
    
    costs = defaultdict(int)
    visited = defaultdict(bool)
    queue = deque()
    queue.append(S)
    costs[mat_to_str(S)] = 0
    visited[mat_to_str(S)] = True
    while len(queue) > 0:
        cur = queue.popleft()
        for u in range(H):
            for d in range(u,H):
                for l in range(W):
                    for r in range(l,W):
                        left_up,right_down = [u,l],[d,r]
                        if left_up == right_down:
                            continue
                        selected_range = [left_up,right_down] # 
                        for direction in [VERTICAL,HORIZONTAL,DIAGONAL,ANTIDIAGONAL]:
                            matrix_t = transpose(cur,selected_range,direction)
                            if equals(matrix_t,T):
                                print(costs[mat_to_str(cur)] + 1)
                                exit()
                            if not visited[mat_to_str(matrix_t)]:
                                queue.append(matrix_t)
                                costs[mat_to_str(matrix_t)] = costs[mat_to_str(cur)] + 1
                                visited[mat_to_str(matrix_t)] = True
    print(-1)

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    T = [list(input()) for _ in range(H)]
    solve(H,W,S,T)