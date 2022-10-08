N,K = map(int,input().split())
A = list(map(int,input().split()))

ok,ng = 0,10**18

def is_possible_project_num(p):

    is_possible = True
    p_num = 0

    for a in A:
        p_num += min(a,p)

    if p * K > p_num:
        is_possible = False

    return is_possible

while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_possible_project_num(mid):
        ok = mid
    else:
        ng = mid    

print(ok)