from collections import deque

N,M = map(int, input().split())
a = []
for i in range(M):
    k =int(input())
    a.append(list(map(int, input().split())))

ball_pos = [[] for i in range(N+1)]

balls_at_head = deque([])

for i in range(M):
    ball_at_head = a[i][-1]
    ball_pos[ball_at_head].append(i)
    if len(ball_pos[ball_at_head]) == 2:
        balls_at_head.append(ball_at_head)

while len(balls_at_head)> 0:
    ball_at_head = balls_at_head.popleft()
    for p in ball_pos[ball_at_head]:
        a[p].pop()
        if len(a[p]) > 0:
            new_ball_at_head = a[p][-1]
            ball_pos[new_ball_at_head].append(p)
            if len(ball_pos[new_ball_at_head]) == 2:
                balls_at_head.append(new_ball_at_head)

ans = True
for i in range(1,N+1):
    if len(ball_pos[i]) != 2:
        ans = False
        break

print("Yes" if ans else "No")