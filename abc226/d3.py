N = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

xy = [list(map(int, input().split())) for _ in range(N)]
magic_dict = {}
for i in range(N):
    for j in range(N):
        if j != i:
            xi, yi = xy[i]
            xj, yj = xy[j]
            gcd_ij = abs(gcd(xi-xj,yi-yj))
            magic = (xi-xj)//gcd_ij, (yi-yj)//gcd_ij
            magic_dict[magic] = True

print(len(magic_dict))




