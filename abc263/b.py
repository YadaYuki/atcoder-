N = int(input())
P = list(map(int,input().split()))
P = [-1] + P
p = N
ans = 0
while p != 1:
    p = P[p-1]
    ans += 1



print(ans)