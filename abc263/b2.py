N = int(input())
P = list(map(int,input().split()))
P = [-1,-1] + P

i = N
ans = 0
while i != 1:
    i = P[i]
    ans += 1
print(ans)