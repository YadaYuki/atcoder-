N,D = map(int, input().split())

walls = []
for _ in range(N):
    walls.append(list(map(int, input().split())))

walls.sort(key=lambda x: x[1]) # sort by 右端の座標

last_punched_idx = -10000000000
ans = 0
for wall in walls:

    if wall[0] <= last_punched_idx + D -1: # 最後にパンチされた範囲の右端よりも、wallの左端の座標が左側に存在する場合、前回のパンチで壊されているため、スキップする。
        continue
    else:
        last_punched_idx = wall[1]
        ans += 1

print(ans)


