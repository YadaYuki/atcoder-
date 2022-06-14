N = int(input())

ans = 0
M = int(N**0.5)
for i in range(1, M+1):
    ans += N // i
ans *= 2
ans -= M**2
print(ans)