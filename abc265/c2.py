H,W = map(int,input().split())
G = [list(input()) for i in range(H)]
visited = [[False for j in range(W)] for i in range(H)]
i,j = (0,0)
while not visited[i][j]:
    visited[i][j] = True
    g = G[i][j]

    is_final_point = (i == 0 and g== "U") or (i == H - 1 and g == "D") or (j == W - 1 and g == "R") or (j == 0 and g == "L")
    if is_final_point:
        print(i+1,j+1)
        exit()

    if g == "U":
        i -= 1
    if g == "D":
        i += 1
    if g == "R":
        j += 1
    if g == "L":
        j -= 1
    

print(-1)

