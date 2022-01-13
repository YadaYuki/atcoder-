N = int(input())
ans = [0] * (N+1) # ans[k]=1~N人がログインしていた日数
LOGIN, LOGOUT = 1, 0
login_logout_day = []
for _ in range(N):
    A,B = map(int,input().split())
    login_logout_day.append([A,LOGIN])    
    login_logout_day.append([A+B,LOGOUT])

login_logout_day.sort()

cur_login_user_num = 0
for i in range(2*N-1):
    d,l = login_logout_day[i]
    if l == LOGIN:
        cur_login_user_num += 1
        ans[cur_login_user_num] += login_logout_day[i+1][0] - d
    else:
        cur_login_user_num -= 1
        ans[cur_login_user_num] += login_logout_day[i+1][0] - d


print(*ans[1:])

