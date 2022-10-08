N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

magic_dict = {}

for i in range(N):
    for j in range(N):
        if i != j:
            xi,yi = xy[i]
            xj,yj = xy[j]
            gcd_ij = abs(gcd(xi-xj,yi-yj))
            magic_dict[((xi-xj)//gcd_ij,(yi-yj)//gcd_ij)] = True


print(len(magic_dict))