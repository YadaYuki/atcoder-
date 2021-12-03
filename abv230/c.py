N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())


def condition_1(i,j): # i,jは1から始まる値
    k_min = max(1-A,1-B)
    k_max = min(N-A,N-B)
    return ((A + k_min <=  i) or (i <= A + k_max)) and (B + k_min <= j <= B + k_max) and (i-A == j-B)

def condition_2(i,j):
    k_min = max(1-A,B-N)
    k_max = min(N-A,B-1)

    return (A + k_min <= i <= A + k_max) and (B - k_max <= j <= B - k_min) and (i-A == B-j)

# condition 1もしくはcondition 2を満たす場合、黒く塗られている。


ans = []

for i in range(P,Q+1):
    x = []
    for j in range(R,S+1):
        if condition_1(i, j) or condition_2(i, j):
            x.append( '#')
        else:
            x.append('.')
    ans.append(x)

for i in range(len(ans)):
    print("".join(ans[i]))


