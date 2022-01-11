import math

N = int(input())

xy = []

def get_distance(a,b):
    xa, ya = a
    xb, yb = b
    return math.sqrt((xa-xb)**2 + (ya-yb)**2)

for _ in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])


ans = -1
for i in range(N-1):
    for j in range(i+1,N):
        ans = max(ans, get_distance(xy[i], xy[j]))
print(ans)