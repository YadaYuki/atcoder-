from collections import defaultdict
S = list(input())
d = defaultdict(int)
for c in S:
    d[c] += 1

if len(d) == 1:
    print(-1)
else:
    for k,v in d.items():
        if v == 1:
            print(k)
            exit()
