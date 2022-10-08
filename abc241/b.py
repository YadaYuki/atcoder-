from collections import defaultdict
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_map = defaultdict(int)
for i in range(N):
    A_map[A[i]] += 1


for i in range(M):
    if A_map[B[i]] == 0:
        print('No')
        exit()
    else:
        A_map[B[i]] -= 1
    
print('Yes')

