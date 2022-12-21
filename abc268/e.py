N = int(input())
p = list(map(int,input().split()))
imos_v,imos_x = [0 for i in range(2*N)],[0 for i in range(2*N)]

for i in range(N):
    stress = (p[i] - i + N) % N
    imos_v[stress] -= stress
    imos_v[stress + N // 2 + 1] += stress
    imos_v[stress + N - (N-1) // 2] += stress + N
    imos_v[N+stress] -= stress + N

    imos_x[stress] += 1
    imos_x[stress + N // 2 + 1] -= 1
    imos_x[stress + N - (N-1) // 2] -= 1
    imos_x[stress+N] += 1

for i in range(2*N-1):
    imos_v[i+1] += imos_v[i]
    imos_x[i+1] += imos_x[i]

ans = 10 ** 24


for i in range(N):
    ans = min(ans,(imos_v[i] + imos_v[i+N]) + (imos_x[i]*i + imos_x[i+N]*(i+N)))

print(ans)