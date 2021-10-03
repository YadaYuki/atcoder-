N,M = map(int,input().split())
S = [0] # 各商品セットの集合を表すnの配列がhairu
C = [0] # 各商品セットの価格が入る

for i in range(M):
    Si,Ci = input().split()
    C.append(int(Ci))
    # Sを集合を表すnに変換
    Si = Si.replace("Y","1").replace("N","0")
    S.append(int(Si,2))

cost = [[float("inf") for _ in range(2**N)] for _ in range(M + 1)]

cost[0][0] = 0

for i in range(1,M+1):
    for j in range(2**N):
        cost[i][j] = min(cost[i][j],cost[i-1][j])
        cost[i][j|S[i]] = min(cost[i][j|S[i]],cost[i-1][j] + C[i])


if cost[M][2**N-1] == float("inf"):
    print(-1)
else:
    print(cost[M][2**N-1])


