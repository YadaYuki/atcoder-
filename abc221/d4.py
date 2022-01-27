N = int(input())

days_change_login_user_num = [] # 一日にログインするユーザ数が変化する日

LOGIN,LOGOUT = 1,0

for _ in range(N):
    A,B = map(int,input().split())
    days_change_login_user_num.append([A,LOGIN])
    days_change_login_user_num.append([A+B,LOGOUT])

D = [0] * (N+1)

days_change_login_user_num.sort() 
login_user_num = 0

for i in range(len(days_change_login_user_num)-1):
    d,l = days_change_login_user_num[i]
    if l == LOGIN:
        login_user_num = login_user_num + 1
    else:
        login_user_num = login_user_num - 1
    D[login_user_num] += days_change_login_user_num[i+1][0] - d

print(*D[1:])



