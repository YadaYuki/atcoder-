N,Q = map(int,input().split())
a = list()
for i in range(N):
    La = list(map(int,input().split()))
    a.append(La[1:])
for i in range(Q):
    s,t = map(int,input().split())
    s-=1
    t-=1
    print(a[s][t])
