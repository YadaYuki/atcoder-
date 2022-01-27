N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

ans = [-1 for _ in range(N)]

ans[0] = T[0]

for i in range(1,N):
    ans[i] = min(ans[i-1] + S[i-1],T[i])

if ans[-1] + S[-1] < ans[0]:
    ans[0] = ans[-1] + S[-1]
    for i in range(1,N):
        ans[i] = min(ans[i-1] + S[i-1],T[i])

for i in range(N):
    print(ans[i])