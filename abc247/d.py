from collections import deque

Q = int(input())

balls_in_cylinder = [] # [[x,c], [x,c], ...]
ball_out= []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _,x,c = query
        if len(balls_in_cylinder) > 0:
            if balls_in_cylinder[-1][0] == x:
                balls_in_cylinder[-1][1] += c
            else:
                balls_in_cylinder.append([x,c])
        else:
            balls_in_cylinder.append([x,c])
    else:
        _,c = query
        ball_out.append(c)

if len(ball_out) == 0:
    exit()


ans = []
ball_out_idx = 0
cur_q2_c = ball_out[ball_out_idx]
ans_q2 = 0
i = 0
while i < len(balls_in_cylinder):
    xq,cq = balls_in_cylinder[i]

    if cq >= cur_q2_c:
        ans.append(ans_q2 + xq * cur_q2_c)
        balls_in_cylinder[i][1] -= cur_q2_c

        ans_q2 = 0
        ball_out_idx += 1
        if ball_out_idx < len(ball_out):
            cur_q2_c = ball_out[ball_out_idx]
        else:
            break
    else:
        ans_q2 += xq * cq
        cur_q2_c -= cq
        i += 1

for i in ans:
    print(i)    
    