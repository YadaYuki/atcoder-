from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))
Q = int(input())

base_v = None
added_by_q2 = defaultdict(int)
ans = []

for _ in range(Q):
    query = list(map(int,input().split()))
    q = query[0]

    if q == 1:
        _,x = query
        base_v = x
        added_by_q2 = defaultdict(int)
    elif q == 2:
        _,i,x = query
        if base_v == None:
            A[i-1] += x
        else:
            added_by_q2[i-1] += x
    elif q == 3:
        _,i = query
        i-=1
        if base_v == None:
            ans.append(A[i])
        else:
            ans.append(base_v + added_by_q2[i])



for a in ans:
    print(a)