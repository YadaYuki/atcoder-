from itertools import permutations
N,M = map(int,input().split())
S = list()
for i in range(N):
    S.append(input())

T = set()
for i in range(M):
    T.add(input())


def dfs(cur_idx: int, left: int, s_candidate,username: str = ""):
    if left < 0:
        return
    if cur_idx == 0:
        s = s_candidate[cur_idx]
        dfs(cur_idx+1,left,s_candidate,s)
        return 
    if cur_idx == N:
        if (not (username in T)) and (len(username) >= 3):
            print(username)
            exit()
        return
    if username[-1] == "_":
        dfs(cur_idx,left-1,s_candidate,username+"_")
        s = s_candidate[cur_idx]
        dfs(cur_idx+1,left,s_candidate,username + s)
    else:
        dfs(cur_idx,left,s_candidate,username+"_")

remain = 16
for sc in S:
    remain -= len(sc)
remain -= (N-1)

S = sorted(S)
for s in permutations(S):
    dfs(0,remain,s)

print(-1)

