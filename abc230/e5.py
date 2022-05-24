N = int(input())
ans = 0
N_sqrt = int(N ** 0.5)
for i in range(1, N_sqrt+1):
    ans += N // i
ans *= 2
ans -= N_sqrt ** 2

print(ans)