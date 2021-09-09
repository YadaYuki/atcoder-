import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())

c = []
for i in range(H):
    c.append(list(input()))


sy, sx, gy, gx = -1, -1, -1, -1
for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            sy, sx = i, j
        if c[i][j] == "g":
            gy, gx = i, j


goto = [[False for _ in range(W)] for _ in range(H)]

goto[sy][sx] = True


def dfs(i, j):
    for i_next_to, j_next_to in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if (not (0 <= i_next_to < H)) or (not (0 <= j_next_to < W)):
          continue
        elif goto[i_next_to][j_next_to] == True:
          continue
        elif c[i_next_to][j_next_to] != "#":
            goto[i_next_to][j_next_to] = True
            dfs(i_next_to, j_next_to)


dfs(sy,sx)


print("Yes" if goto[gy][gx] == True else "No")
