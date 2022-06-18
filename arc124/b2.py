import sys
N = int(input())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

xs = set()
for i in range(N):
    xs.add(a[0] ^ b[i])

ans = []
b.sort()
for x in xs:
    c = [x^a[i] for i in range(N)]
    c.sort()
    ok = True
    for i in range(N):
        if b[i] != c[i]:
            ok = False
    if ok:
        ans.append(x)

ans.sort()
print(len(ans))
for i in ans:
    print(i)