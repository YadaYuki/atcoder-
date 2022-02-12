from collections import deque

N,M = map(int,input().split())
balls_in_cylinders = []
cylinders_has_balls = [[] for _ in range(N+1)] # 各ボールをが何番目のシリンダーに入っているかを保存
for i in range(M):
    k = int(input())
    balls_in_cylinder = list(map(int,input().split()))
    balls_in_cylinders.append(balls_in_cylinder)
    cylinders_has_balls[balls_in_cylinder[-1]].append(i)


queue = deque([])

for i in range(N+1):
    if len(cylinders_has_balls[i]) == 2:
        queue.append(i)

while len(queue) > 0:
    ball_in_head = queue.popleft()
    for cylinder in cylinders_has_balls[ball_in_head]:
        balls_in_cylinders[cylinder].pop()
        if len(balls_in_cylinders[cylinder]) > 0:
            new_ball_in_head = balls_in_cylinders[cylinder][-1]
            cylinders_has_balls[new_ball_in_head].append(cylinder)
            if len(cylinders_has_balls[new_ball_in_head]) == 2:
                queue.append(new_ball_in_head)


is_ok = True

for i in range(1,N+1):
    if len(cylinders_has_balls[i]) != 2:
        is_ok = False
        break

if is_ok:
    print("Yes")
else:
    print("No")

