
# 右端の座標でソートして、右端を殴る.


N,D = map(int,input().split())


LR = [list(map(int,input().split())) for _ in range(N)]
LR.sort(key=lambda x:x[1])


ans = 0
last_punth_x = -1
for i in range(N):
    lr = LR[i]
    if lr[0] <= last_punth_x:
        continue
    else:
        ans += 1
        last_punth_x = lr[1] + D - 1


print(ans)