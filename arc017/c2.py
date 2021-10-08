from collections import defaultdict

N, X = map(int, input().split())
weight_group_A, weight_group_B = [], []

for i in range(N):
    w = int(input())
    if i % 2 == 0:
        weight_group_A.append(w)
    else:
        weight_group_B.append(w)
A_num, B_num = len(weight_group_A), len(weight_group_B)

A_ALL, B_ALL = 2 ** A_num, 2**B_num

def has_bit(n,i):
    return (n & (1 << i) > 0)

weight_dict_A = defaultdict(int)

for n in range(A_ALL):
    s = 0
    for i in range(A_num+1):
        if has_bit(n, i):
            s += weight_group_A[i-1]
    weight_dict_A[s] += 1



ans = 0
for n in range(B_ALL):
    s = 0
    for i in range(B_num + 1):
        if has_bit(n,i):
            s += weight_group_B[i-1]
    
    ans += weight_dict_A[X-s]

print(ans)



