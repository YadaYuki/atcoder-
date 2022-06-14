N,D = map(int,input().split())


LR = [list(map(int,input().split())) for _ in range(N)]

LR.sort(key=lambda x:x[1])
ans = 1
last_punched_idx = LR[0][1]

for i in range(1,N):
    if  last_punched_idx + D > LR[i][0]:
        continue
    else:
        ans += 1
        last_punched_idx = LR[i][1]




print(ans)
