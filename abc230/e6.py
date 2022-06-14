N = int(input())
N_sqrt = int(N ** 0.5)
ans = 0
for i in range(1,N_sqrt+1):
    
    ans += N // i

ans *= 2
ans -= N_sqrt ** 2

print(ans)
