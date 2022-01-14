# https://atcoder.jp/contests/abc228/submissions/28276698

from sys import setrecursionlimit, stdin
 
setrecursionlimit(1000000)
 

q = int(stdin.readline().rstrip())
query = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(q)]
n = 1 << 20
ans = [-1 for _ in range(n)] # N= 2 ** 20からなる数列を初期化.
root = [-1] * n

def find(x):
    if root[x] < 0:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x,y):
    rx = find(x)
    ry = find(y)
    if rx != ry:
        root[ry] = rx
    
    

for t,x in query:
    h = x % n
    if t==1:
        if ans[h] == -1:
            ans[h] = x
            continue
        while True:
            h = find(h) + 1
            if h == n:
                h = 0
                if ans[h] == -1:
                    break
                continue
            union(h,h-1)
            if ans[h] == -1:
                break
        ans[h] = x

    else:
        print(ans[h])