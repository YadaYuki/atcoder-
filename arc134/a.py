import math

N,L,W = map(int,input().split())
a = list(map(int,input().split()))

covered_section_arr = [[-1,0]] # [0,0]はダミー

for i in range(N):
    covered_section_arr.append([a[i],a[i] + W])

covered_section_arr.append([L,-1]) # これもダミー

ans = 0

for i in range(len(covered_section_arr)-1):
    if covered_section_arr[i+1][0] - covered_section_arr[i][1] > 0:
        ans += -(-(covered_section_arr[i+1][0] - covered_section_arr[i][1])//W)


print(ans)