from collections import deque

N,M = map(int,input().split())
cylinders_state = []

for i in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    cylinders_state.append(a)


balls_at_head_to_cylinders_idx = [[] for i in range(N + 1)]

balls_two_cylinders_at_head = deque()

for i in range(M):
    ball_at_head = cylinders_state[i][-1]
    balls_at_head_to_cylinders_idx[ball_at_head].append(i)
    if len(balls_at_head_to_cylinders_idx[ball_at_head]) == 2:
        balls_two_cylinders_at_head.append(ball_at_head)

while len(balls_two_cylinders_at_head) > 0:
    ball_two_cylinders_at_head = balls_two_cylinders_at_head.popleft()
    for cylinder in balls_at_head_to_cylinders_idx[ball_two_cylinders_at_head]:
        cylinders_state[cylinder].pop() 
        if len(cylinders_state[cylinder]) > 0:
            new_ball_at_head = cylinders_state[cylinder][-1]
            balls_at_head_to_cylinders_idx[new_ball_at_head].append(cylinder)
            if len(balls_at_head_to_cylinders_idx[new_ball_at_head]) == 2:
                balls_two_cylinders_at_head.append(new_ball_at_head)


for cylinder in cylinders_state:
    if len(cylinder) != 0:
        print('No')
        exit()

print('Yes')
