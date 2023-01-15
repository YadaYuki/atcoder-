from collections import deque
N,M = map(int,input().split())

BIG = 10 ** 18
costs = [[-1 for i in range(N)] for j in range(N)]


diff = list()

for x in range(0,int(M**0.5)+1):
    M_tmp = M
    M_tmp -= x ** 2
    y = int(M_tmp ** 0.5)
    if (x * x + y * y) == M:
        diff.append([x,y])
        diff.append([x,-y])
        diff.append([-x,y])
        diff.append([-x,-y])

q = deque([(0,0)])
costs[0][0] = 0

while len(q) != 0:
    cur = q.popleft()
    cx,cy = cur
    for dx,dy in diff:
        nx,ny = cx + dx, cy + dy
        if 0 <= nx < N and 0 <= ny < N:
            visited = costs[nx][ny] != -1
            if visited:
                continue
            costs[nx][ny] = costs[cx][cy] + 1
            q.append((nx,ny))



for d in costs:
    print(*d)


