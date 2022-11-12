N,K = map(int,input().split())
A = list(map(int,input().split()))
R = -1

xy = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    dist_to_nearest_light = 1e10
    for k in range(K):
        a = A[k]
        a -= 1
        xa,ya = xy[a]
        xi,yi = xy[i]
        dist_to_nearest_light = min(((xi-xa) ** 2 + (yi-ya)**2) ** 0.5,dist_to_nearest_light)
    
    R = max(R,dist_to_nearest_light)
        




print(R)