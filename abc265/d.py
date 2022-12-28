N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))

A_sum = [0]
for i in range(N):
    A_sum.append(A_sum[-1] + A[i])

P_pair_map = {}
r = 0
v = 0
for l in range(N):

    while r < N and (v < P):
        v += A[r]
        r += 1
    
    if v == P:
        P_pair_map[l] = r-1
    v -= A[l]

Q_pair_map = {}
r = 0
v = 0
for l in range(N):

    while r < N and (v < Q):
        v += A[r]
        r += 1
    
    if v == Q:
        Q_pair_map[l] = r-1
    v -= A[l]

R_pair_map = {}
r = 0
v = 0
for l in range(N):

    while r < N and (v < R):
        v += A[r]
        r += 1
    
    if v == R:
        R_pair_map[l] = r-1
    v -= A[l]


for xs,xe in P_pair_map.items():
    if (xe+1) in Q_pair_map:
        ye = Q_pair_map[xe+1]
        if ye+1 in R_pair_map:
            print("Yes")
            exit()

print("No")