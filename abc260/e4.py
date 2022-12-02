N,M = map(int,input().split())
A,B = [],[]
A_2_B = [-1] * (M + 1) 

for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    A_2_B[a] = max(A_2_B[a],b)

imos = [0 for i in range(M+2)]

B_min = min(B)
r = max(A)
for l in range(1,B_min+1):
    min_length = r-l+1
    maximum_length = M-l+1
    imos[min_length] += 1
    imos[maximum_length+1] -= 1
    if A_2_B[l] > 0:
        r = max(r,A_2_B[l])
for i in range(M+1):
    imos[i+1] += imos[i]

print(*imos[1:M+1])

