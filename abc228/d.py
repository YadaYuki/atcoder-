N = 2**20
Q = int(input())
A = [-1 for _ in range(N)]
P = [(i+1)%N for i in range(N)]

for i in range(Q):
    t,x = map(int,input().split())
    h = x % N
    if t == 1:
        l = [h]
        while A[h] != -1:
            h = P[h]
            l.append(h)
        A[h] = x
        for j in l:
            P[j] = P[h]
    else:
        print(A[h])


