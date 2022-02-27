# ref:https://atcoder.jp/contests/abc236/submissions/28981582
N = int(input())
A = [[0 for _ in range(2*N)] for _ in range(2*N)]
for i in range(2*N-1):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        A[i][j+i+1] = a[j]
        A[j+i+1][i] = a[j]


used = [False for _ in range(2*N)]
ans = -1
def dfs(happiness):
    global ans
    if sum(used) == 2 * N:
        # print(ans,happiness)
        ans =  max(ans,happiness)
    else:
        # ペアの一人目を選ぶ
        p1 = -1
        for i in range(2*N):
            if not used[i]:
                p1 = i
                used[i] = True
                break
        # print(p1,happiness,used)
        # ペアの二人目を選ぶ
        for i in range(2*N):
            if not used[i]:
                p2 = i
                used[p2] = True
                dfs(happiness ^ A[p1][p2])
                used[p2] = False
        used[p1] = False


dfs(0)
print(ans)