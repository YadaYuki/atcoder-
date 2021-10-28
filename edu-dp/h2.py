H,W = map(int,input().split())

grid = []

for _ in range(H):
    grid.append(list(input()))

MOD = 10 ** 9 + 7

patterns = [[0 for _ in range(W)] for _ in range(H)]

patterns[0][0] = 1


for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            continue
        if i == 0 and j==0:
            continue
        elif i == 0:
            patterns[i][j] = patterns[i][j-1]
        elif j == 0:
            patterns[i][j] = patterns[i-1][j]
        
        else:
            patterns[i][j] = (patterns[i][j-1] + patterns[i-1][j]) % MOD

print(patterns[H-1][W-1])


