N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# cost[i][j]:すでに訪れた都市の集合がi,訪れた最後の都市がj
cost = [[float("inf") for _ in range(N)] for _ in range(2**N)]

def has_bit(n,i):
    return (n & (1 << i) > 0)

cost[0][0] = 0

for i in range(2**N):
    for j in range(N): # すでにおとづれた都市がi,都市jから都市kへと移動する。
        for k in range(N):
            if has_bit(i,k) or j == k:
                continue
            cost[i|1<<k][k] = min(cost[i|1<<k][k],cost[i][j] + A[j][k])

print(cost[2**N-1][0])
            


