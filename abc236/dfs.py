

ans = []
N = 8
count = [2] * N
perm = [0] * (2*N)
def dfs(depth,size):
    if depth == size:
        ans.append(perm)
    else:
        for i in range(N*2):
            if count[i//2] > 0:
                perm[depth] = i // 2
                count[i//2] -= 1
                dfs(depth+1,size)
                count[i//2] += 1

dfs(0,2*N)
print(ans)