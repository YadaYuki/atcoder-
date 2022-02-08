from itertools import permutations


N = int(input())

A = []
enjoy_score_mat = [[0] * 2*N for _ in range(2*N)]
for _ in range(2*N-1):
    A.append(list(map(int, input().split())))

for i in range(2*N-1):
    for j in range(i+1,2*N):
        enjoy_score_mat[i][j] = A[i][j-i-1]
        enjoy_score_mat[j][i] = A[i][j-i-1]

def get_enjoy_score(pairs):
    pair1 = pairs[0]
    total_enjoy_score = enjoy_score_mat[pair1[0]][pair1[1]]
    for i in range(1,len(pairs)):
        pair = pairs[i]
        enjoy_score = enjoy_score_mat[pair[0]][pair[1]]
        total_enjoy_score ^= enjoy_score

    return total_enjoy_score

def get_pair_list(N,perm):
    pairs_list = []
    for perm in perm_map:
        pairs = [[] for _ in range(N)]
        for i in range(2*N):
            pairs[perm[i]].append(i)
        pairs_list.append(pairs)
    return pairs_list


perms = []
perm = [0] * (2*N)
count = [2] * N
def dfs(depth,size):
    if depth == size:
        perms.append(perm[:])
    else:
        for i in range(N*2):
            if count[i//2] > 0:
                perm[depth] = i // 2
                count[i//2] -= 1
                dfs(depth+1,size)
                count[i//2] += 1



dfs(0,2*N)
pairs = get_pair_list(N,perms) # [[[0,1],[2,3]],[[0,2],[1,3]],[[0,3],[1,2]]] 

ans = -1
for i in range(len(pairs)):
    ans = max(ans,get_enjoy_score(pairs[i]))

print(ans)
