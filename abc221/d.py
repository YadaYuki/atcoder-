
N = int(input())
# ログインした日付・ログアウトした日付を格納する
date_login_logout = []

for _ in range(N):
    A,B = map(int,input().split())
    login = [A,1]
    logout = [A+B,-1]
    date_login_logout.append(login)
    date_login_logout.append(logout)


date_login_logout.sort() 

ans = [0 for _ in range(N)] # k人がログインしていた日数を格納


count = 0


for i in range(len(date_login_logout)-1): #date_login_logoutの長さは、2*N.
    count += date_login_logout[i][1]
    ans[count-1] += date_login_logout[i+1][0] - date_login_logout[i][0] # 次にログイン・ログアウトされるまではログインユーザー数は一定であるため、その日数を加算する。

for i in range(N):
    print("{} ".format(ans[i]),end="")

