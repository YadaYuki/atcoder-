from bisect import bisect_right
N,K = map(int,input().split())
A = list(map(int,input().split()))
A_map = {a:True for a in  A}
dp = {
    "Takahashi":[0 for i in range(N+1)],
    "Aoki":[0 for i in range(N+1)]
}
for p in ["Takahashi","Aoki"]:
    for i in range(N+1):
        if i in  A_map:
            dp[p][i] = i
people = ["Takahashi","Aoki"]
for left_stone in range(1,N+1):
    for a in A:
        for i,p in enumerate(people):
            if left_stone > a:
                next_p_stone = dp[people[1-i]][left_stone-a]
                dp[p][left_stone] = max(dp[p][left_stone],left_stone-dp[p][left_stone-a])

        
print(dp["Takahashi"][-1])
