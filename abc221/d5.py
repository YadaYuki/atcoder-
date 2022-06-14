N = int(input())
login_logout_days = []
LOGIN, LOGOUT = 0, 1

for _ in range(N):
    A,B = map(int, input().split())
    login_logout_days.append([A, LOGIN])
    login_logout_days.append([A+B, LOGOUT])

ans = [0 for _ in range(N+1)]
l = 0
login_logout_days.sort()
for i in range(len(login_logout_days)-1):
    d,login_logout = login_logout_days[i]
    # if log
    if login_logout == LOGIN:
        l += 1
    else:
        l -= 1
    ans[l] += login_logout_days[i+1][0] - d
        

print(*ans[1:])