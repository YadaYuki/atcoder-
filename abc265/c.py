H,W = map(int,input().split())
G = [list(input()) for i in range(H)]
visited = [[False for i in range(W)] for j in range(H)]

def is_last(i,j,g):
    return (i == 0 and g == "U") or (i == (H-1) and g == "D") or (j == 0 and g == "L") or (j == W-1 and g == "R")

i,j, = 0,0
while not (is_last(i, j, G[i][j])):
    if visited[i][j]:
        print(-1)
        exit()
    g = G[i][j]
    visited[i][j] = True
    if g == "U":
        i -= 1
    if g == "D":
        i += 1
    if g == "L":
        j -= 1
    if g == "R":
        j += 1


print((i+1),(j+1))
    
