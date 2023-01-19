from collections import deque
N,M = map(int,input().split())
diff = []
for k in range(int(M**0.5)+1):
    l = int((M - (k*k))**0.5)
    if (l * l + k * k) == M:
        diff.append((k,l))
        diff.append((-k,l))
        diff.append((k,-l))
        diff.append((-k,-l))

ans = [[-1 for i in range(N)] for j in range(N)]
q = deque([(0,0)])
ans[0][0] = 0
while len(q) > 0:
    cur = q.popleft()
    for d in diff:
        cx,cy = cur
        dx,dy = d
        nx,ny = cx+dx, cy+dy
        if 0 <= nx < N and 0 <= ny < N:
            if ans[nx][ny] == -1:
                ans[nx][ny] = ans[cx][cy] + 1
                q.append((nx,ny))

for a in ans:
    print(*a)
