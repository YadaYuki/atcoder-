def has_bit(n,i):
    return (n & (1 << i) > 0)

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

PATTERN_NUM = 2 ** N
BIG = 10 ** 100

cost = [[BIG for _ in range(N)] for _ in range(PATTERN_NUM)]

# 始点から終点としての0へのコストは0であるため、初期化
cost[0][0] = 0

for n in range(PATTERN_NUM):
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            cost[n|1<<j][j] = min(cost[n|1<<j][j],cost[n][i] + A[i][j])

print(cost[PATTERN_NUM-1][0])