N = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

magic_dict = {}

xy = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            # iからjに移動する魔法の中でその絶対値が最小のものを計算する.
            xi,yi = xy[i]
            xj,yj = xy[j]
            g = abs(gcd(xi-xj,yi-yj))
            magic = (xi-xj)//g , (yi-yj)//g
            magic_dict[magic] = True
print(len(magic_dict))

