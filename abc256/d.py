import bisect
N = int(input())
L,R = 0,1
ranges = [] #  

for i in range(N):
    l,r = map(int,input().split())
    ranges.append([l,L])
    ranges.append([r,R])

ranges.sort()
ans = []
l = 0
r = 1
ranges_size = 2 * N
for i in ranges:


for i in ans:
    print(*i)