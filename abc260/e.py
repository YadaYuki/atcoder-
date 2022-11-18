N,M = map(int,input().split())
pair = [0]*(M+1)
imos = [0]*(M+2)
Amax = 0
Bmin = 10**10

for _ in range(N):
    a,b = map(int,input().split())
    pair[a] = max(pair[a],b)
    Amax = max(Amax,a)
    Bmin = min(Bmin,b)

r = Amax
for l in range(1,Bmin+1):
    imos[r-l+1] += 1 # r - l の長さに該当するやつを + する
    imos[M-l+2] -= 1 
    if pair[l] > 0: # lに対して、pairが存在するとき
        r = max(r,pair[l])

for i in range(1,M+1):
    imos[i] += imos[i-1]

print(*imos[1:M+1])