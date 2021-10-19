N,M = map(int,input().split())

MOD = 10 ** 9  + 7

broken = [False] * (N + 1)

for _ in range(M):
    a = int(input())
    broken[a] = True

patterns = [0] * (N+1)

patterns[0] = 1
patterns[1] = 1

for i in range(2,N+1):
    if not broken[i]:
        patterns[i] = (patterns[i-1] + patterns[i-2]) % MOD

print(patterns[N])