S = list(input())
T = list(input())
N = len(S)
for i in range(N):
    if S[i] != T[i]:
        print(i+1)
        exit()

print(N+1)