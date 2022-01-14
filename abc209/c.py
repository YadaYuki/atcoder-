MOD = 10 ** 9 + 7

N = int(input())
C = list(map(int, input().split()))


C.sort()

ans = 1
for i in range(N):
    ans = ans * (C[i] - i) % MOD
    
print(ans)