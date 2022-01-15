N,D = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(N)]

LR.sort(key=lambda x:x[1]) # 右端の座標でソートして、


last_panched = LR[0][1]
ans = 1
for i in range(1,N):
    if LR[i][0] >= last_panched + D:
        last_panched = LR[i][1] # 左端(L)をパンチする
        ans += 1
    else:
        continue

print(ans)


