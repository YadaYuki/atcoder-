L,R = map(int,input().split())
S = list(input())

S_L_to_R = S[L-1:R]
ans = []

for i in range(L-1):
    ans.append(S[i])

for i in range(len(S_L_to_R)-1,-1,-1):
    ans.append(S_L_to_R[i])

for i in range(R,len(S)):
    ans.append(S[i])

print(''.join(ans))





