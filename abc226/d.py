import ast

N = int(input())
magic_dict = {}

coordinates = []

def gcd(a,b):
    '''
    Calculate gretest common divisor by euclid mutual division method
    '''
    if b == 0:
        return a
    return gcd(b,a%b)



for _ in range(N):
    x,y = map(int,input().split())
    coordinates.append((x,y))

for i in range(N):
    for j in range(N):
        if i != j: # i,jが相異なる場合は、移動するための魔法を産出する
            coordinate_i,coordinate_j = coordinates[i],coordinates[j]
            a = coordinate_i[0] - coordinate_j[0]
            b = coordinate_i[1] - coordinate_j[1]
            # 方向ベクトルを求める。
            gcd_ab = abs(gcd(a,b))
            
            magic_dict[str((int(a/gcd_ab),int(b/gcd_ab)))] = True


print(len(magic_dict))



