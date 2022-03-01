N = int(input())
S = input()

R,L = [],[]
for i in range(N-1,-1,-1):
    if S[i] == 'R':
        L.append(i)
    else:
        R.append(i)


print(*L[::-1],N,*R)
