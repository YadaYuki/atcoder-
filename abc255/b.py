N,K = map(int,input().split())
A = list(map(int,input().split()))
delighted = [0] * N
for i in range(K):
    delighted[A[i]-1] = 1

delighted_xy = []
not_delighted_xy = []

for i in range(N):
    x,y = map(int,input().split())
    if delighted[i]:
        delighted_xy.append([x,y])
    else:
        not_delighted_xy.append([x,y])

R = -1
def get_distance(a,b):
    xa,ya = a
    xb,yb = b
    return ((xa-xb) ** 2 + (ya-yb)** 2) ** 0.5

for x,y in not_delighted_xy:
    min_R = 10 ** 9
    for xd,yd in delighted_xy:
        a = [x,y]
        b = [xd,yd]
        min_R = min(min_R,get_distance(a, b))
    R = max(R,min_R)

print(R)