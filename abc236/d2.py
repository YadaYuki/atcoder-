# ref:https://atcoder.jp/contests/abc236/submissions/28981582
N = int(input())
A = [[0 for _ in range(2*N)] for _ in range(2*N)]
for i in range(2*N-1):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        A[i][j+i+1] = a[j]
        A[j+i+1][i] = a[j]


ans = 0
used = [False]*(2*N)

def dfs(depth,happiness):
    global ans
    if depth == N:
        ans = max(ans, happiness)
        return
    i = 0
    while used[i]:
        i += 1
    used[i] = True
    for j in range(i+1,2*N):
        if not used[j]:
            used[j] = True
            dfs(depth+1, happiness^A[i][j])
            used[j] = False
    
    used[i] = False

dfs(0,0)

print(ans)