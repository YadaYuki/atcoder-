import math
R,X,Y = map(int,input().split())
rxy = (X ** 2 + Y ** 2) ** 0.5

print(math.ceil(rxy/R))
