import sys
sys.setrecursionlimit(1000000)

N = int(input())
time_to_master = []
need_to_master = []
mastered = [False for _ in range(N)]

for i in range(N):
    arr = list(map(int,input().split()))
    time_to_master.append(arr[0])
    a = arr[2:]
    for i in range(arr[1]):
        a[i] -= 1
    need_to_master.append(a)


def master_techniques(technique:int):
    
    if not mastered[technique]:
        mastered[technique] = True
        for technique_to_master in need_to_master[technique]:
            master_techniques(technique_to_master)

master_techniques(N-1)
ans = 0

for i in range(N):
    ans += mastered[i] * time_to_master[i]

print(ans)
    

