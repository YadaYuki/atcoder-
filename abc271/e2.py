N,M,K = map(int,input().split())
A,B,C = list(),list(),list()

for i in range(M):
    a,b,c = map(int,input().split())
    A.append(a-1)
    B.append(b-1)
    C.append(c)


E = list(map(int,input().split()))
BIG = 10 ** 19
cost_to_i = [BIG for i in range(N)]
cost_to_i[0] = 0
for i in range(K):
    e = E[i] - 1
    cost_to_i[B[e]] = min(cost_to_i[B[e]],cost_to_i[A[e]] + C[e])

if cost_to_i[N-1] == BIG:
    print(-1)
else:
    print(cost_to_i[N-1])