N,D = map(int,input().split())
walls = []

for _ in range(N):
    walls.append(list(map(int,input().split())))

walls.sort(key=lambda x: x[1]) # 左端の座標でソート

# 右端を殴る
punched = 1
last_punched_pos = walls[0][1]
for i in range(1,N):
    if walls[i][0] < last_punched_pos + D:
        continue
    else:
        punched += 1
        last_punched_pos = walls[i][1]
print(punched)