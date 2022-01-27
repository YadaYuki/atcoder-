import sys
sys.setrecursionlimit(10**6)

H,W = map(int,input().split())

C = [list(input()) for _ in range(H)]

count_walk = [[-1 for _ in range(W)] for _ in range(H)]

def dfs(h,w):
    is_next_h_wall = h == H-1 or C[h+1][w] == '#'
    is_next_w_wall = w == W-1 or C[h][w+1] == '#'
    if is_next_h_wall and is_next_w_wall:
        count_walk[h][w] = 1
        
        return count_walk[h][w]
    
    elif is_next_h_wall:
        if count_walk[h][w+1] == -1:
            count_walk[h][w+1] = dfs(h,w+1) 
        
        return count_walk[h][w+1] + 1
    
    elif is_next_w_wall:
        if count_walk[h+1][w] == -1:
            count_walk[h+1][w] = dfs(h+1,w)

        return count_walk[h+1][w] + 1
    
    else:
    
        if count_walk[h+1][w] == -1:
            count_walk[h+1][w] = dfs(h+1,w)
    
        if count_walk[h][w+1] == -1:
            count_walk[h][w+1] = dfs(h,w+1)
    
        return max(count_walk[h+1][w],count_walk[h][w+1]) + 1



print(dfs(0,0))

