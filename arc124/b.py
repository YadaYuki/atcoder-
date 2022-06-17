import sys
N = int(input())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
x_to_idx_set_map = {}

for i in range(N):
    for j in range(N):
        x = a[i] ^ b[j]
        if x in x_to_idx_set_map:
            if not (j in x_to_idx_set_map[x]):
                x_to_idx_set_map[x].add(j)
        else:
            x_to_idx_set_map[x] = set([j])


ans = []
for k,v in x_to_idx_set_map.items():
    if len(v) == N:
        ans.append(k)
ans.sort()
print(len(ans))
for i in ans:
    print(i)