N = int(input())

M = int(N ** 0.5)

ans = 0

for i in range(1,M+1):
    ans += N // i
ans *= 2
ans -= M ** 2
print(ans)