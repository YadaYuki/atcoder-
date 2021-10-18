N = int(input())

happy = []
for _ in range(N):
    a,b = map(int,input().split())
    happy.append([-a-b,a,b])

happy.sort()

ans = 0

for i in range(N):
    _,a,b = happy[i]
    if i % 2 == 0:
        ans += a
    else:
        ans -= b

print(ans)
