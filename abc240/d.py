N = int(input())
a = list(map(int, input().split()))
balls_in_cylinder = [] #[[ボールの種類,ボールの個数],[ボールの種類,ボールの個数],...]
cur_ball_num = 0
ans = []
for i in range(N):
    if len(balls_in_cylinder) == 0:
        balls_in_cylinder.append([a[i],1])
        cur_ball_num += 1
    else:
        ball,count = balls_in_cylinder[-1]
        if a[i] == ball:
            balls_in_cylinder[-1][1] += 1
        else:
            balls_in_cylinder.append([a[i],1])
        cur_ball_num += 1
        
        ball,count = balls_in_cylinder[-1]
        if ball == count:
                balls_in_cylinder.pop()
                cur_ball_num -= ball
    
    ans.append(cur_ball_num)
    
for i in ans:
    print(i)
