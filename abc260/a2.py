from collections import defaultdict
S = list(input())
m = defaultdict(int)
for c in S:
    m[c] += 1

for k,v in m.items():
    if v == 1:
        print(k)
        exit()

print(-1)