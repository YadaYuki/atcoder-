H,W = map(int,input().split())
C = [list(input()) for _ in range(H)]

ans = [[-1 for _ in range(W)] for _ in range(H)]

def dfs(i,j):
    is_next_h_wall = i == H-1
    if not is_next_h_wall:
        is_next_h_wall = C[i+1][j] == '#'
    is_next_w_wall = j == W-1
    if not is_next_w_wall:
        is_next_w_wall = C[i][j+1] == '#'
    
    if is_next_h_wall and is_next_w_wall:
        ans[i][j] = 1
        return 1
    elif is_next_h_wall:
        if ans[i][j+1] == -1:
            ans[i][j+1] = dfs(i,j+1)    
        return ans[i][j+1] + 1
    elif is_next_w_wall:
        if ans[i+1][j] == -1:
            ans[i+1][j] = dfs(i+1,j)
        return ans[i+1][j] + 1
        
    else:
        if ans[i+1][j] == -1:
            ans[i+1][j] = dfs(i+1,j)
        if ans[i][j+1] == -1:
            ans[i][j+1] = dfs(i,j+1)
        return max(ans[i+1][j],ans[i][j+1]) + 1

print(dfs(0,0))
