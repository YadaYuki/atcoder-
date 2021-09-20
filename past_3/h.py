N, L = map(int, input().split())
x = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())
hurdle = [False for _ in range(L+1)]

for i in range(N):
    hurdle[x[i]] = True

cost = [float("inf")] * (L+1)
cost[0] = 0

cost_action1, cost_action2, cost_action3 = T1, T1 + T2, T1+3 * T2

for i in range(1, L+1):
    cost[i] = min(cost[i], cost[i-1] + cost_action1)  # 座標iへのコスト
    if i >= 2:
        cost[i] = min(cost[i], cost[i-2] + cost_action2)  # 座標iへのコスト
    if i >= 4:
        cost[i] = min(cost[i], cost[i-4] + cost_action3)  # 座標iへのコスト
    cost[i] += T3 * hurdle[i]

# ジャンプの途中でゴールした場合

ans = cost[L]

ans = min(ans, hurdle[L-1] * T3 + cost[L-1]+int(0.5+0.5*(T1+T2)))
ans = min(ans, hurdle[L-2] * T3 + cost[L-2]+int(0.5+0.5*T1+1.5*T2))
ans = min(ans, hurdle[L-3] * T3 + cost[L-3]+int(0.5+0.5*T1+2.5*T2))
# 必ず整数である、という条件を間違えていた..！
print(ans)
