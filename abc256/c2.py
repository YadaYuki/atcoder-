H,W = map(int,input().split())
G = [list(input()) for i in range(H)]
visited = [[False for i in range(W)] for j in range(H)]

ok = False
i,j = 0,0
while not visited[i][j]:
    g = G[i][j]
    visited[i][j] = True
    if g == "U":
        if i == 0:
            print(f"{i+1} {j+1}")
            exit()
        i -= 1
    if g == "D":
        if i == H - 1:
            print(f"{i+1} {j+1}")
            exit()
        i += 1
    if g == "L":
        if j == 0:
            print(f"{i+1} {j+1}")
            exit()
        j -= 1
    if g == "R":
        if j == W - 1:
            print(f"{i+1} {j+1}")
            exit()
        j += 1

print(-1)


