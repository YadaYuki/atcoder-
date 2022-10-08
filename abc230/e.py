from math import sqrt,ceil,floor

N = int(input())
M = int(sqrt(N))
ans = 0
# print(M)
for i in range(1,M+1):
    ans += N//i
ans *= 2
ans -= M**2
print(ans)