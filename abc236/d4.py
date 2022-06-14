N = int(input())
A = [[0 for _ in range(2*N)] for _ in range(2*N)]

for i in range(2*N-1):
    a = list(map(int, input().split()))
    for j in range(i+1,2*N):
        A[i][j] = A[j][i] = a[j-i-1]


used = [False for _ in range(2*N)]
ans = -1

def dfs(h):
    if sum(used) == 2 * N:
        global ans
        ans = max(ans, h)
    
    else:
        p1,p2 = -1,-1
        for p in range(2*N):
            if not used[p]:
                p1 = p
                used[p1] = True
                break

        for p in range(2*N):
            if not used[p]:
                p2 = p
                used[p2] = True
                dfs(h ^ A[p1][p2])
                used[p2] = False
        used[p1] = False


dfs(0)
print(ans)