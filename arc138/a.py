from functools import cmp_to_key
from collections import defaultdict
N,K = map(int,input().split())
A = list(map(int,input().split()))
first_kth_dict = defaultdict(int)
min_first_kth = min(A[:K])

possible = False
for i in range(K,N):
    if A[i] > min_first_kth:
        possible = True
        break


if not possible: # 目標は達成できない
    print(-1)
else:
    A_idxes = [[A[i],i] for i in range(N)]
    def cmp(x, y):
        if x[0] == y[0]:
            return x[1] - y[1]
        return  y[0] - x[0]
    A_idxes.sort(key=cmp_to_key(cmp))
    BIG = 4 * 10 ** 5 + 1
    ans = BIG
    i_candidate = -1
    j_candidate = -1
    ij_candidates = []
    for i in range(N):
        a,idx = A_idxes[i]
        if idx >= K:
            if j_candidate != -1:
                ans = min(ans,idx - j_candidate)
        else:
            j_candidate = max(j_candidate,idx)
    
    print(ans)
        
    
    
