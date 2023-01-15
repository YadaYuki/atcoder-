N = int(input())
S = list(input())
ans = list()
for i in range(N-1):
    k = 0
    while ((k+i+1) < N) and (S[k] != S[k+i+1]):
        k += 1
    ans.append(k)

for a in ans:
    print(a)