
N,K = map(int,input().split())
A = list(map(int,input().split()))

dp = {
    "Takahashi":[0 for i in range(N+1)],
    "Aoki":[0 for i in range(N+1)]
}

for a in A:
    dp["Takahashi"][a] = a
    dp["Aoki"][a] = a

persons = ["Takahashi","Aoki"]
for left_cnt in range(N+1):
    for j,p in enumerate(persons):
        for a in A:
            if left_cnt >= a:
                another_p = persons[1-j]
                dp[p][left_cnt] = max(left_cnt-dp[another_p][left_cnt-a],dp[p][left_cnt])
            else:
                break

print(dp["Takahashi"][-1])


