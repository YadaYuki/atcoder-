N = int(input())
ans = []
d = {}
for i in range(N):
    s = input()
    if s in d:
        d[s] += 1
        s = f"{s}({d[s]-1})"
    else:
        d[s] = 1
    ans.append(s)

for a in ans:
    print(a)