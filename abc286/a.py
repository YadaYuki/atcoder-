N,P,Q,R,S = map(int,input().split())
A = list(map(int,input().split()))
B = A.copy()
for i in range(Q-P+1):
    B[i+(P-1)] = A[i+(R-1)]

for i in range(Q-P+1):
    B[i+(R-1)] = A[i+(P-1)]

print(*B)