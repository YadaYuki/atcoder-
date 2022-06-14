from  collections import defaultdict
N,K = map(int,input().split())

def binary_str(n):
    return bin(n)[2:]
S_arr = []
for i in range(N):
    S_arr.append(input())
ans = -1
for i in range(2**N):
    bin_arr = list(reversed(binary_str(i)))
    patterns = []
    for i,bit in enumerate(bin_arr):
        if bit == '1':
            patterns.append(S_arr[i])
    d = defaultdict(int)
    for s in patterns:
        for c in s:
            d[c] += 1
    count = 0
    for c in d:
        if d[c] == K:
            count += 1
    ans = max(ans,count)
print(ans)

