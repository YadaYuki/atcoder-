def gcd(a,b):
    '''
    Calculate gretest common divisor by euclid mutual division method
    '''
    if b == 0:
        return a
    return gcd(b,a%b)


magic_dict = {}

N = int(input())

coordinetes = []

for i in range(N):
    X,Y = map(int,input().split())
    coordinetes.append([X,Y])


for i in range(N):
    for j in range(N):
        if i != j:
            Xi,Yi = coordinetes[i]
            Xj,Yj = coordinetes[j]
            a = Xi-Xj
            b = Yi-Yj
            gcd_ab = abs(gcd(a,b))
            magic = (int(a/gcd_ab),int(b/gcd_ab))
            magic_dict[str(magic)] = True

print(len(magic_dict))


