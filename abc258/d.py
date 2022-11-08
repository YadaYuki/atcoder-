N,X = map(int,input().split())

# cost_base = 0
A = []
B = []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

cost_base = 0
B_min = 5e18
ans = 5e18
for i in range(N):
    a,b = A[i],B[i]
    cost_base += a + b
    B_min = min(B_min,b)
    stage_base = i + 1
    # 残りのステージをB_minでやるのが最良
    if stage_base > X:
        break
    ans = min(ans,B_min * (X - stage_base) + cost_base)

print(ans)
