L,R = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

i_to = min(L+1500,R+1)
j_from = max(R-1500,L+1)
ans= -1
for i in range(L,i_to):
    for j in range(j_from,R+1):
        if j > i:
            if gcd(i,j) == 1:
                ans = max(ans,j-i)
            

print(ans)
