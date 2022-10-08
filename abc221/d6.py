N = int(input())

LOGIN,LOGOUT = 1,0
days_change_login_count = []

for _ in range(N):
    a,b = map(int,input().split())
    days_change_login_count.append([a,LOGIN])
    days_change_login_count.append([a+b,LOGOUT])


days_change_login_count.sort()

D = [0] * (N + 1)
cur = 0
for i in range(2*N-1):
    d,login_logout = days_change_login_count[i]
    dn,_ = days_change_login_count[i+1]
    if login_logout == LOGIN:
        cur += 1
    else:
        cur -= 1
    D[cur] += dn - d

print(*D[1:])