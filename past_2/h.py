N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(input()))

# 各マス目が存在する座標の位置を配列として格納したデータ

coordinates = [[] for _ in range(11)]
for i in range(N):
    for j in range(M):
        if A[i][j] == "S":
            A[i][j] = "0"
        elif A[i][j] == "G":
            A[i][j] = "10"
        coordinates[int(A[i][j])].append([i, j])

cost = [[float("inf") for _ in range(M)] for _ in range(N)]

cost[coordinates[0][0][0]][coordinates[0][0][1]] = 0

# コストを動的計画法により計算する
for i in range(1, 11):
    for j in range(len(coordinates[i])):
        for k in range(len(coordinates[i-1])):
            i2, j2 = coordinates[i-1][k]
            cost[coordinates[i][j][0]][coordinates[i][j][1]] = min(cost[coordinates[i][j][0]][coordinates[i][j][1]], cost[i2][j2] + abs(
                i2-coordinates[i][j][0])+abs(j2-coordinates[i][j][1]))

if cost[coordinates[10][0][0]][coordinates[10][0][1]] == float("inf"):
  print(-1)
else:
  print(cost[coordinates[10][0][0]][coordinates[10][0][1]])
