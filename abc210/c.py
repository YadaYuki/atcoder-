import math

N = int(input())
A = list(map(int,input().split()))
X = int(input())
sum_A = sum(A)

ans = N * (math.floor(X/sum_A))

X = X % sum_A

# Xに至るまで,Aを探索

cur_sum = 0

i = 0
for i in range(N):
    cur_sum += A[i]
    if cur_sum > X:
        ans += i + 1
        break

print(ans)

