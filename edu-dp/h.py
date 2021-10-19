H,W = map(int,input().split())
is_wall = [[False for _ in range(W)] for _ in range(H)]

for i in range(H):
    a = input()
    for j in range(W):
        if a[j] == "#":
            is_wall[i][j] = True

route = [[0 for _ in range(W)] for _ in range(H)]

route[0][0] = 1

MOD = 10 ** 9 + 7

for i in range(H):
    for j in range(W):
        if is_wall[i][j]:
            continue
        if i == 0 and j == 0:
            continue
        elif i == 0:
            route[i][j] = route[i][j-1]
        elif j == 0:
            route[i][j] = route[i-1][j]
        else:
            route[i][j] = (route[i-1][j] + route[i][j-1]) % MOD

print(route[H-1][W-1])

