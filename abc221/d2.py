N = int(input())

date_change_login_player_num = [] # ログインしているユーザーの数が変換するタイミングとそれがログイン（+1）によるものか。ろぐあうと(-1)によるものかを格納した配列

for _ in range(N):
    A,B = map(int,input().split())
    date_change_login_player_num.append([A,"login"])
    date_change_login_player_num.append([A+B,"logout"])

date_change_login_player_num.sort() 

ans = [] # k(0 ~ N)人がログインしている日数を
for _ in range(N+1):
    ans.append(0)


login_user_num = 0
for i in range(2*N-1):
    date,login_logout = date_change_login_player_num[i]
    if login_logout == "login":
        login_user_num += 1
        # 次にログイン・ログアウトが生じるまでユーザ数は一定
    else:
        login_user_num -= 1
    ans[login_user_num] += date_change_login_player_num[i+1][0] - date_change_login_player_num[i][0]

    
for i in range(1,N+1):
    print(ans[i],end=" ")


