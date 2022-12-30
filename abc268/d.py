from itertools import permutations

N,M = map(int,input().split())
S = [input() for i in range(N)]
T = [input() for i in range(M)]
T_set = set(T)

def dfs(cur_username,used_S_cnt,s,remain):
    if remain < 0:
        return 
    if used_S_cnt == N:
        if len(cur_username) >= 3 and (not cur_username in T_set):
            print(cur_username)
            exit()
        return
    else:
        if len(cur_username) > 0 and cur_username[-1] != "_":
            dfs(cur_username + "_",used_S_cnt,s,remain)
        else:
            dfs(cur_username + sc[used_S_cnt],used_S_cnt+1,s,remain)
            if len(cur_username) > 0:
                dfs(cur_username+"_",used_S_cnt,s,remain-1)


remain = 16
for sc in S:
    remain -= len(sc)
remain -= (N-1)
S = sorted(S)
for sc in permutations(S):
    dfs("",0,sc,remain)

print(-1)


